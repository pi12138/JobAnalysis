import os
import json
from collections import defaultdict

from company.models import JobPosition, Label, Company
from company.constants import JobDirection, VERBOSE_NAME_TO_JOB_DIRECTION, EDUCATION_VERBOSE_NAME_TO_VALUE, Education

"""
usage:
    python manage.py runscript import_job_info
"""


def get_label_name_to_label():
    queryset = Label.objects.all()
    return {i.name: i for i in queryset}


def get_company_name_to_company():
    queryset = Company.objects.all()
    return {i.name: i for i in queryset}


def get_job_uuid_to_job_position():
    queryset = JobPosition.objects.all().select_related('company')
    return {'{}-{}'.format(job.company.name, job.name) for job in queryset}


def set_label_for_job_position(job_uuid_to_skill_labels, job_uuid_to_welfare_labels):
    queryset = JobPosition.objects.all().select_related('company')
    for job in queryset:
        job_uuid = '{}-{}'.format(job.company.name, job.name)
        skill_labels = job_uuid_to_skill_labels.get(job_uuid, [])
        welfare_labels = job_uuid_to_welfare_labels.get(job_uuid, [])
        job.skill_label.set(skill_labels)
        job.welfare_label.set(welfare_labels)


def run():
    base_path = './data/'
    file_list = os.listdir(base_path)
    # job_info_list = list()
    job_direction_to_job_list = dict()
    existed_job_queryset = JobPosition.objects.all().values_list('company__name', 'name')
    existed_job_uuid_set = {'{}-{}'.format(job[0], job[1]) for job in existed_job_queryset}
    label_name_to_label = get_label_name_to_label()
    company_name_to_company = get_company_name_to_company()

    for filename in file_list:
        full_path = base_path + filename
        split_list = filename.split('.')[0].split('_')
        if len(split_list) == 1:
            continue
        job_direction = split_list[1]

        with open(full_path, 'r') as file:
            file_data = file.read()
            file_data = file_data.replace(' ', '').replace('\n', '')
            file_data = json.loads(file_data)
            # job_info_list.extend(file_data)
            job_direction_to_job_list[job_direction] = file_data

    job_position_list = list()
    job_uuid_to_skill_labels = defaultdict(list)
    job_uuid_to_welfare_labels = defaultdict(list)
    for job_direction, job_list in job_direction_to_job_list.items():
        for job in job_list:
            job_uuid = '{}-{}'.format(job['company_info'], job['name'])

            skill_label = job['skill_label']
            welfare_label = job['welfare_label']
            skill_label_instance_list = list()
            welfare_label_instance_list = list()
            for skill in skill_label:
                skill_instance = label_name_to_label.get(skill)
                if skill_instance:
                    skill_label_instance_list.append(skill_instance)
                    job_uuid_to_skill_labels[job_uuid].append(skill_instance)
            for welfare in welfare_label:
                welfare_instance = label_name_to_label.get(welfare)
                if welfare_instance:
                    welfare_label_instance_list.append(welfare_instance)
                    job_uuid_to_welfare_labels[job_uuid].append(welfare_instance)

            if job_uuid in existed_job_uuid_set:
                continue

            company_name = job['company_info']
            company_instance = company_name_to_company.get(company_name)
            job_direction_value = VERBOSE_NAME_TO_JOB_DIRECTION.get(job_direction)

            job_position_list.append(JobPosition(
                name=job['name'],
                location=job['location'],
                # welfare_label=welfare_label_instance_list,
                salary=job['salary'],
                work_experience=job['work_experience'],
                education=EDUCATION_VERBOSE_NAME_TO_VALUE.get(job['education'], Education.OTHER),
                # skill_label=skill_label_instance_list,
                company=company_instance,
                job_direction=job_direction_value
            ))

    print('一共要创建{}条数据'.format(len(job_position_list)))
    save = input('是否保存y/n: ')
    if save == 'y':
        JobPosition.objects.bulk_create(job_position_list, batch_size=1000)
        print('创建成功')
    else:
        print('什么也没有执行')

    print('为JobPosition设置Label')
    set_label_for_job_position(job_uuid_to_skill_labels, job_uuid_to_welfare_labels)
    print('设置成功')

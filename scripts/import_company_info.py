import os
import json

from company.models import Company

"""
usage:
    python manage.py runscript import_company_info
"""


def run():
    base_path = './data/'
    file_list = os.listdir(base_path)
    company_name_set = set()
    existed_company_name_set = Company.objects.all().values_list('name', flat=True)
    existed_company_name_set = set(existed_company_name_set)

    for filename in file_list:
        full_path = base_path + filename

        with open(full_path, 'r') as file:
            file_data = file.read()
            file_data = file_data.replace(' ', '').replace('\n', '')
            file_data = json.loads(file_data)
            for data in file_data:
                if data.get('company_info'):
                    company_name_set.add(data.get('company_info'))

    new_create_company_name_set = company_name_set - existed_company_name_set
    new_company_list = list()
    for name in new_create_company_name_set:
        new_company_list.append(Company(name=name))

    print('即将创建{}条数据'.format(len(new_company_list)))
    save = input('是否保存y/n: ')
    if save == 'y':
        Company.objects.bulk_create(new_company_list, batch_size=1000)
        print('创建成功')
    else:
        print('什么也没有执行')

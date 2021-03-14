import os
import json

from company.models import Label
from company.constants import LabelType


"""
usage:
    python manage.py runscript import_label
"""


def run():
    base_path = './data/'
    filename_list = os.listdir(base_path)
    existed_skill_label_name = Label.objects.filter(label_type=LabelType.SKILL).values_list('name', flat=True)
    existed_welfare_label_name = Label.objects.filter(label_type=LabelType.WELFARE).values_list('name', flat=True)
    label_key = ['skill_label', 'welfare_label']
    new_skill_label_list = list()
    new_welfare_label_name_list = list()
    skill_label_name_set = set()
    welfare_label_name_set = set()

    for filename in filename_list:
        full_path = '{}{}'.format(base_path, filename)

        with open(full_path, 'r') as file:
            file_data = file.read()
            file_data = file_data.replace('\n', '').replace(' ', '')
            data_list = json.loads(file_data)

            for data in data_list:
                skill_labels = data[label_key[0]]
                welfare_labels = data[label_key[1]]
                skill_label_name_set.update(skill_labels)
                welfare_label_name_set.update(welfare_labels)

    dont_existed_skill_label_name = skill_label_name_set - set(existed_skill_label_name)
    dont_existed_welfare_label_name = welfare_label_name_set - set(existed_welfare_label_name)

    for label_name in dont_existed_skill_label_name:
        new_skill_label_list.append(Label(name=label_name, label_type=LabelType.SKILL))
    for label_name in dont_existed_welfare_label_name:
        new_welfare_label_name_list.append(Label(name=label_name, label_type=LabelType.WELFARE))

    print('一个有{}个新标签要生成.'.format(len(new_welfare_label_name_list+new_skill_label_list)))
    save = input('是否要保存y/n:')
    if save == 'y':
        Label.objects.bulk_create(new_skill_label_list+new_welfare_label_name_list, batch_size=1000)

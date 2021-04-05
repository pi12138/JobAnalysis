from django.db.models import Count

from company.models import JobPosition, Label
from company.constants import JOB_DIRECTION_TO_VERBOSE_NAME


class JobPositionService:
    @classmethod
    def get_job_direction_analysis(cls, elements):
        element_list = elements.split(',')
        job_position_qs = JobPosition.objects.filter(
            job_direction__in=element_list
        ).values('job_direction').annotate(total=Count('id'))

        result = list()
        for job in job_position_qs:
            result.append(
                {
                    'name': JOB_DIRECTION_TO_VERBOSE_NAME.get(job['job_direction']),
                    'value': job['total']
                }
            )
        return result

    @classmethod
    def get_welfare_label_analysis(cls, elements):
        element_list = elements.split(',')
        job_position_qs = JobPosition.objects.filter(
            welfare_label__id__in=element_list
        ).values('welfare_label').annotate(total=Count('id'))

        label_qs = Label.objects.filter(id__in=element_list)
        label_id_to_label = {label.id: label for label in label_qs}
        result = list()
        for job in job_position_qs:
            label_id = job['welfare_label']
            label = label_id_to_label.get(label_id)
            if label is None:
                continue
            result.append(
                {
                    'name': label.name,
                    'value': job['total']
                }
            )
        return result

    @classmethod
    def get_skill_label_analysis(cls, elements):
        element_list = elements.split(',')
        job_position_qs = JobPosition.objects.filter(
            skill_label__id__in=element_list
        ).values('skill_label').annotate(total=Count('id'))

        label_qs = Label.objects.filter(id__in=element_list)
        label_id_to_label = {label.id: label for label in label_qs}
        result = list()
        for job in job_position_qs:
            label_id = job['skill_label']
            label = label_id_to_label.get(label_id)
            if label is None:
                continue
            result.append(
                {
                    'name': label.name,
                    'value': job['total']
                }
            )
        return result

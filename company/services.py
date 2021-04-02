from django.db.models import Count

from company.models import JobPosition
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

from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from django_filters.rest_framework import DjangoFilterBackend

# from company.api.filters import JobPositionFilterBackend
from company.api.filters import JobPositionFilterSet
from company.models import JobPosition, Label
from company.constants import JOB_DIRECTION_TO_VERBOSE_NAME, AnalysisType, LabelType
from company.api.serializers import JobPositionListSerializer
from company.api.paginations import JobPositionPagination
from company.services import JobPositionService


class JobPositionViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = JobPosition.objects.all()
    pagination_class = JobPositionPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = JobPositionFilterSet

    def get_serializer_class(self):
        if self.action in ['list']:
            serializer_class = JobPositionListSerializer
        else:
            raise Exception()

        return serializer_class

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='job-direction')
    def job_direction(self, request, *args, **kwargs):
        result = list()
        for key, value in JOB_DIRECTION_TO_VERBOSE_NAME.items():
            result.append({'key': key, 'name': value})
        return Response(result)

    @action(methods=['GET'], detail=False, url_path='welfare-label')
    def welfare_label(self, request, *args, **kwargs):
        result = list()
        label_qs = Label.objects.filter(
            label_type=LabelType.WELFARE
        )
        for label in label_qs:
            result.append(
                {
                    'key': label.id,
                    'name': label.name
                }
            )
        return Response(result)

    @action(methods=['GET'], detail=False, url_path='skill-label')
    def skill_label(self, request, *args, **kwargs):
        result = list()
        label_qs = Label.objects.filter(
            label_type=LabelType.SKILL
        )
        for label in label_qs:
            result.append(
                {
                    'key': label.id,
                    'name': label.name
                }
            )
        return Response(result)

    @action(methods=['GET'], detail=False, url_path='analysis')
    def analysis(self, request, *args, **kwargs):
        analysis_type = int(request.query_params.get('analysis_type'))
        elements = request.query_params.get('elements')
        if not elements:
            return Response([])
        if analysis_type == AnalysisType.JOB_DIRECTION:
            result = JobPositionService.get_job_direction_analysis(elements)
        elif analysis_type == AnalysisType.WELFARE_LABEL:
            result = JobPositionService.get_welfare_label_analysis(elements)
        elif analysis_type == AnalysisType.SKILL_LABEL:
            result = JobPositionService.get_skill_label_analysis(elements)
        else:
            raise APIException(detail='错误的分析类别')

        count = 0
        for ele in result:
            count += ele['value']

        for ele in result:
            ele['percent'] = '{:.2%}'.format( ele['value'] / count)

        return Response(result)

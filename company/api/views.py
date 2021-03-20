from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# from company.api.filters import JobPositionFilterBackend
from company.api.filters import JobPositionFilterSet
from company.models import JobPosition
from company.api.serializers import JobPositionListSerializer
from company.api.paginations import JobPositionPagination


class JobPositionViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = JobPosition.objects.all()
    pagination_class = JobPositionPagination
    filter_backends = [DjangoFilterBackend]
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
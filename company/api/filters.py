from rest_framework.filters import BaseFilterBackend
from django_filters import rest_framework as filters

from company.models import JobPosition

#
# class JobPositionFilterBackend(BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         name = request.query_params.get('name')
#
#         if name:
#             queryset = queryset.filter(name__icontains=name)
#         return queryset


class JobPositionFilterSet(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = JobPosition
        fields = []
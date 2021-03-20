from rest_framework import pagination


class JobPositionPagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_param = 'page'

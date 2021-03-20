from rest_framework.routers import DefaultRouter

from company.api.views import JobPositionViewSet


router = DefaultRouter()
router.register(r'job-position', JobPositionViewSet, basename='job-position')

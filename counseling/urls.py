from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CounselingScheduleAPI, CounselingResultAPI

router = DefaultRouter()
router.register('schedule', CounselingScheduleAPI, basename='counseling_schedule')
router.register('result', CounselingResultAPI, basename='counseling_result')

urlpatterns = [
    path('', include(router.urls))
]

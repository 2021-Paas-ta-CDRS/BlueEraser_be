from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchingAPI, PackageAPI, ReviewAPI

router = DefaultRouter()
router.register(r'matching/(?P<matching_id>\d+)/review', ReviewAPI, basename='review')
router.register(r'matching', MatchingAPI, basename='matching')
router.register(r'', PackageAPI, basename='package')

urlpatterns = [
    path('', include(router.urls)),
]

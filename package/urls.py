from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchingAPI, PackageAPI

router = DefaultRouter()
router.register(r'', PackageAPI, basename='package')
router.register(r'mathcing', MatchingAPI, basename='matching')

urlpatterns = [
    path('', include(router.urls)),
]

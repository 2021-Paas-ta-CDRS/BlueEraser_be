from django.urls import path, include
from rest_framework.routers import DefaultRouter
from package.views import PackageAPI

router = DefaultRouter()
router.register(r'', PackageAPI, basename='package')

urlpatterns = [
    path('', include(router.urls))
]

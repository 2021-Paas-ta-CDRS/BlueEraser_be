from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateAPI, CreateDoctorAPI, GetDoctorAPI, UpdateDoctorAPI
from package.views import PackageAPI

router = DefaultRouter()
router.register(r'certificate', CertificateAPI, basename='certificate')
router.register(r'package', PackageAPI, basename='package')

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    path('update/', UpdateDoctorAPI.as_view()),
    path('', GetDoctorAPI.as_view()),

    path('', include(router.urls)),
]

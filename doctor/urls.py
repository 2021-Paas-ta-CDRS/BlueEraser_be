from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateAPI, CreateDoctorAPI, DoctorAPI, ReadOnlyCertificateAPI, UpdateDoctorAPI
from package.views import ReadOnlyPackageAPI

router = DefaultRouter()
router.register(r'', DoctorAPI, basename='doctor')
router.register(r'certificates', CertificateAPI, basename='certificate')
router.register(r'(?P<doctor_id>\d+)/certificates', ReadOnlyCertificateAPI, basename='doctor_certificates')
router.register(r'(?P<doctor_id>\d+)/packages', ReadOnlyPackageAPI, basename='doctor_packages')

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    path('update/', UpdateDoctorAPI.as_view()),
    path('', include(router.urls)),
]

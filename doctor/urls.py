from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateAPI, CreateDoctorAPI, DoctorAPI, ReadOnlyCertificateAPI, UpdateDoctorAPI
from package.views import ReadOnlyPackageAPI, ReadOnlyReviewAPI, ReviewAPI

router = DefaultRouter()
router.register(r'', DoctorAPI, basename='doctor')
router.register(r'certificates', CertificateAPI, basename='certificate')
router.register(r'(?P<doctor_id>\d+)/certificate', ReadOnlyCertificateAPI, basename='doctor_certificates')
router.register(r'(?P<doctor_id>\d+)/package', ReadOnlyPackageAPI, basename='doctor_packages')
router.register(r'package/(?P<package_id>\d+)/review', ReviewAPI, basename='review')
router.register(r'(?P<doctor_id>\d+)/review', ReadOnlyReviewAPI, basename='read_only_review')

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    path('update/', UpdateDoctorAPI.as_view()),
    path('', include(router.urls)),
]

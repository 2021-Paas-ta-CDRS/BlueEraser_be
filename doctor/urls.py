from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateAPI, CreateDoctorAPI, DoctorAPI, ReadOnlyDoctorAPI, ReadOnlyCertificateAPI, UpdateDoctorAPI
from package.views import ReadOnlyPackageAPI, ReadOnlyReviewAPI

router = DefaultRouter()
router.register(r'certificate', CertificateAPI, basename='certificate')
router.register(r'(?P<doctor_id>\d+)/certificate', ReadOnlyCertificateAPI, basename='doctor_certificate')
router.register(r'(?P<doctor_id>\d+)/package', ReadOnlyPackageAPI, basename='doctor_package')
router.register(r'(?P<doctor_id>\d+)/review', ReadOnlyReviewAPI, basename='read_only_review')
router.register(r'update', UpdateDoctorAPI, basename='doctor_update')
router.register(r'info', DoctorAPI, basename='doctor')
router.register(r'', ReadOnlyDoctorAPI, basename='read_only_doctor')

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    # path('update/', UpdateDoctorAPI.as_view()),
    path('', include(router.urls)),
]

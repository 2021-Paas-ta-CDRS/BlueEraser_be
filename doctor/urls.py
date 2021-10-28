from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateAPI, CreateDoctorAPI, GetDoctorAPI, UpdateDoctorAPI

router = DefaultRouter()
router.register(r'', CertificateAPI, basename='certificate')

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    path('update/', UpdateDoctorAPI.as_view()),
    path('', GetDoctorAPI.as_view()),

    path('certificate/', include(router.urls)),
]

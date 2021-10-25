from django.urls import path, include

from patient.models import Patient
from .views import CreatePatientAPI, GetPatientAPI, LoginPatientAPI, UpdatePatientAPI

urlpatterns = [
    path('signup/', CreatePatientAPI.as_view()),
    path('login/', LoginPatientAPI.as_view()),
    path('update/', UpdatePatientAPI.as_view()),
    path('', GetPatientAPI.as_view()),
]

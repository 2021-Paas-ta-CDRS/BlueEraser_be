from django.urls import path, include
from .views import CreatePatientAPI, GetPatientAPI, UpdatePatientAPI

urlpatterns = [
    path('signup/', CreatePatientAPI.as_view()),
    path('update/', UpdatePatientAPI.as_view()),
    path('', GetPatientAPI.as_view()),
]

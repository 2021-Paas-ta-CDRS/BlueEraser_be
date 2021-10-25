from django.urls import path, include
from .views import CreateDoctorAPI, UpdateDoctorAPI

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    path('update/', UpdateDoctorAPI.as_view()),
]

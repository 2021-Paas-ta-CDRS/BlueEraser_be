from django.urls import path, include
from .views import CreateDoctorAPI, GetDoctorAPI, UpdateDoctorAPI

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    path('update/', UpdateDoctorAPI.as_view()),
    path('', GetDoctorAPI.as_view()),
]

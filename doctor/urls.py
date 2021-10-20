from django.urls import path, include
from .views import CreateDoctorAPI, LoginDoctorAPI
from rest_framework import urls

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
    path('login/', LoginDoctorAPI.as_view()),
]

from django.urls import path, include
from .views import CreatePatientAPI, LoginPatientAPI, UpdatePatientAPI

urlpatterns = [
    path('signup/', CreatePatientAPI.as_view()),
    path('login/', LoginPatientAPI.as_view()),
    path('update/', UpdatePatientAPI.as_view()),
]

from django.urls import path, include
from .views import CreatePatientAPI

urlpatterns = [
    path('signup/', CreatePatientAPI.as_view()),
]

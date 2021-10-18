from django.urls import path, include
from .views import CreateDoctorAPI

urlpatterns = [
    path('signup/', CreateDoctorAPI.as_view()),
]

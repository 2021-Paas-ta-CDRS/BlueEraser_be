from django.urls import path, include
from .views import CreatePatientAPI, GetPatientAPI, UpdatePatientAPI

urlpatterns = [
    path('signup/', CreatePatientAPI.as_view()),  # POST
    path('update/', UpdatePatientAPI.as_view()),  # PUT
    path('', GetPatientAPI.as_view()),            # GET
]

from rest_framework import generics
from .serializer import CreatePatientSerializer
from .models import Patient

class CreatePatientAPI(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = CreatePatientSerializer

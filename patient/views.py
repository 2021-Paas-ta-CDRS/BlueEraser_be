from rest_framework import generics
from user.models import User
from .serializers import CreatePatientSerializer

class CreatePatientAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreatePatientSerializer

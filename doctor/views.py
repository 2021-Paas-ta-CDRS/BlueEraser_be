from django.db.models import query
from rest_framework import generics
from user.models import User
from .serializers import CreateDoctorSerializer

class CreateDoctorAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateDoctorSerializer

from rest_framework import generics
from .serializers import CreateUserSerializer
from .models import User

class CreateUserAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    
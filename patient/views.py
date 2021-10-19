from rest_framework import generics, status
from rest_framework.response import Response
from user.serializers import CreateUserSerializer
from knox.models import AuthToken

class CreatePatientAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(user_type='P')
        return Response(status=status.HTTP_201_CREATED)

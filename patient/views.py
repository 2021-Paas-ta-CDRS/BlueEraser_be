from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from patient.serializers import UpdatePatientSerializer
from user.serializers import CreateUserSerializer, LoginUserSerializer


class CreatePatientAPI(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'user_type': 'P', **request.data.dict()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginPatientAPI(CreateAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny]


class UpdatePatientAPI(CreateAPIView):
    serializer_class = UpdatePatientSerializer
    permission_classes = [AllowAny]

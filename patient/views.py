from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from patient.serializers import UpdatePatientSerializer
from user.serializers import CreateUserSerializer, LoginUserSerializer


@permission_classes([AllowAny])
class CreatePatientAPI(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'user_type': 'P', **request.data.dict()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@permission_classes([AllowAny])
class LoginPatientAPI(CreateAPIView):
    serializer_class = LoginUserSerializer


@permission_classes([IsAuthenticated])
class UpdatePatientAPI(CreateAPIView):
    serializer_class = UpdatePatientSerializer

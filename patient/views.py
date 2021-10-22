from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from patient.serializers import UpdatePatientSerializer
from user.serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer

@permission_classes([AllowAny])
class CreatePatientAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(user_type='P')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class LoginPatientAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                'email': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data.get('email'),
                'token': user['token']
            }
        )

@permission_classes([IsAuthenticated])
class UpdatePatientAPI(generics.GenericAPIView):
    serializer_class = UpdatePatientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

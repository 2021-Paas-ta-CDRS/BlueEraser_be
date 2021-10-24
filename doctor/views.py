from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from user.serializers import CreateUserSerializer, LoginUserSerializer, UpdateUserSerializer, UserSerializer
from .serializers import UpdateDoctorSerializer

@permission_classes([AllowAny])
class CreateDoctorAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_type='D')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class LoginDoctorAPI(generics.GenericAPIView):
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
class UpdateDoctorAPI(generics.GenericAPIView):
    serializer_class = UpdateDoctorSerializer
    user_serializer_class = UpdateUserSerializer

    def put(self, request, *args, **kwargs):
        request_data = self.get_data_with_userid(request)
        serializer = self.serializer_class(data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update_or_create()

        user_serializer = self.user_serializer_class(request.user, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def get_data_with_userid(self, request):
        return {'user': request.user.id, **request.data.dict()}

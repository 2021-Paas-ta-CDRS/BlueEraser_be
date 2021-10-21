from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginUserSerializer, UpdateUserSerializer, UserSerializer

@permission_classes([AllowAny])
class LoginUserAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        if user['email'] == 'None':
            return Response({'message': 'login failed'}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_data = UserSerializer(user, context=self.get_serializer_context()).data
        return Response(
            {
                'email': user_data.get('email'),
                'token': user['token'],
            }
        )

@permission_classes([IsAuthenticated])
class UpdateUserAPI(generics.GenericAPIView):
    serializer_class = UpdateUserSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
 
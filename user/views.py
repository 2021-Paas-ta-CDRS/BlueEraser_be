from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginUserSerializer, UserSerializer

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
class TestTokenAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return Response({'message': 'user authenticated!'}, status=status.HTTP_200_OK)

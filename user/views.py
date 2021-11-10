from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.models import User
from .serializers import GetUserTypeSerializer, LoginUserSerializer, UserSerializer

class LoginUserAPI(GenericAPIView):
    permission_classes = [AllowAny]
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

class GetUserTypeAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserTypeSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

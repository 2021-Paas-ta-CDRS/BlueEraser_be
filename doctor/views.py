from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from doctor.models import Certificate, Doctor
from .serializers import CertificateSerializer, DoctorSerializer, UpdateDoctorSerializer
from user.serializers import CreateUserSerializer, UpdateUserSerializer

class CreateDoctorAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'user_type': 'D', **request.data.dict()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UpdateDoctorAPI(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateDoctorSerializer
    user_serializer_class = UpdateUserSerializer

    def update(self, request, *args, **kwargs):
        request_data = self.get_data_with_userid(request)
        serializer = self.serializer_class(data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update_or_create()

        user_serializer = self.user_serializer_class(request.user, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def get_data_with_userid(self, request):
        return {'user_id': request.user.id, **request.data.dict()}

class GetDoctorAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)

class CertificateAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CertificateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'doctor': request.user.doctor, **request.data.dict()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return Certificate.objects.filter(doctor=self.request.user.doctor)

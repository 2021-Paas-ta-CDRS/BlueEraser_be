from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from doctor.models import Certificate, Doctor
from .serializers import CertificateSerializer, DoctorSerializer, ReadOnlyDoctorSerializer, UpdateDoctorSerializer
from user.serializers import CreateUserSerializer, UpdateUserSerializer

class CreateDoctorAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'user_type': 'D', **request.data})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UpdateDoctorAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateDoctorSerializer
    user_serializer_class = UpdateUserSerializer

    def create(self, request, *args, **kwargs):
        request_data = self.get_data_with_userid(request)
        serializer = self.serializer_class(data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update_or_create()

        user_serializer = self.user_serializer_class(request.user, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response((user_serializer.data, serializer.data), status=status.HTTP_200_OK)
    
    def get_data_with_userid(self, request):
        return {'user_id': request.user.id, **request.data}

class ReadOnlyDoctorAPI(ReadOnlyModelViewSet):
    """ 의사 조회 API
        비로그인 상태 의사 정보를 조회하는 API
        Note:
            * List, Retrieve
                List        모든 의사의 정보를 조회한다.
                Retreive    특정 의사의 정보를 조회한다. Path params 사용.
            * GET method만 허용한다.
    """
    permission_classes = [AllowAny]
    serializer_class = ReadOnlyDoctorSerializer

    def get_queryset(self):
            return Doctor.objects.all()

class DoctorAPI(ReadOnlyModelViewSet):
    """ 의사 조회 API
        로그인 상태 의사 정보를 조회하는 API
        Note:
            * List
                List    현재 로그인한 본인(의사)의 정보를 조회한다.
            * GET method만 허용한다.
    """
    
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer
    
    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)

class CertificateAPI(ModelViewSet):
    """ 자격증 API(의사)
        의사에게 호출되는 상품 API
        Note:
            * header Authorization 파라미터가 필요하다.
            * prefix가 doctor인 url에서 호출된다.
                ex) */doctor/certificate/
                    */doctor/certificate/1/
            * GET, POST, DELETE, PUT을 허용한다.
    """
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

class ReadOnlyCertificateAPI(ReadOnlyModelViewSet):
    """ 자격증 API (비로그인 또는 환자)
        비로그인 사용자와 환자에게 호출되는 자격증 API
        Note:
            * prefix가 doctor인 url에서 호출된다.
                ex) */doctor/<int:doctor_id>/certificates/
                    */doctor/<int:doctor_id>/certificates/1/
            * GET method만 허용한다.
    """
    permission_classes = [AllowAny]
    serializer_class = CertificateSerializer

    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return Certificate.objects.filter(doctor=doctor_id)

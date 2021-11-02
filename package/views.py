from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from package.models import Matching, Package

from package.serializers import MatchingSerializer, PackageSerializer

class PackageAPI(ModelViewSet):
    """ 상품 API (의사)
        의사에게 호출되는 상품 API
        Note:
            * header에 Authorization 파라미터가 필요하다.
            * prefix가 package인 url에서 호출된다.
                ex) */package/
                    */package/1/
            * GET, POST, DELETE, PUT을 허용한다.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PackageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'doctor': request.user.doctor, **request.data.dict()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_queryset(self):
        return Package.objects.filter(doctor=self.request.user.doctor)

class ReadOnlyPackageAPI(ReadOnlyModelViewSet):
    """ 상품 API (비로그인 또는 환자)
        비로그인 사용자와 환자에게 호출되는 상품 API
        Note:
            * prefix가 doctor인 url에서 호출된다.
                ex) */doctor/<int:id>/packages/
                    */doctor/<int:id>/packages/1/
            * GET method만 허용한다.
    """
    permission_classes = [AllowAny]
    serializer_class = PackageSerializer

    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return Package.objects.filter(doctor=doctor_id)

class MatchingAPI(ModelViewSet):
    """ 매칭 API (의사 및 환자)
        의사 및 환자에게 호출되는 매칭 API
        Note:
            * prefix가 package인 url에서 호출된다.
                ex) */package/matching/
                    */package/matching/1
            * GET, POST, DELETE, PUT을 허용한다.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MatchingSerializer

    def create(self, request, *args, **kwargs):
        if hasattr(self.request.user, 'doctor'):
            return PermissionDenied()
        serializer = self.get_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        current_user = self.request.user
        if hasattr(current_user, 'doctor'):
            return Matching.objects.filter(package=current_user.doctor.package)
        elif hasattr(current_user, 'patient'):
            return Matching.objects.filter(patient=current_user.patient)
        else:
            raise PermissionDenied()

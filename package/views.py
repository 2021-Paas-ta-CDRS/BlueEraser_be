from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from package.models import Matching, Package, Review

from package.serializers import MatchingSerializer, PackageSerializer, ReviewSerializer

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
        serializer = self.get_serializer(data={'doctor': request.user.doctor, **request.data})
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
                ex) */doctor/<int:doctor_id>/packages/
                    */doctor/<int:doctor_id>/packages/1/
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
                    */package/matching/1/
            * GET, POST, DELETE, PUT을 허용한다.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MatchingSerializer

    def create(self, request, *args, **kwargs):
        if hasattr(self.request.user, 'doctor'): 
            # 의사가 post 할 경우 permission deny
            return PermissionDenied()
        serializer = self.get_serializer(data={'patient': request.user.patient, **request.data})
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

class ReviewAPI(ModelViewSet):
    """ 리뷰 API (환자)
        환자에게 호출되는 리뷰 API
        Note:
            * prefix가 doctor/matching/인 url에서 호출된다.
                ex) doctor/matching/<int:matching_id>/review/
                    doctor/matching/<int:matching_id>/review/1
            * GET, POST, DELETE, PUT을 허용한다.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        doctor = self.get_doctor_id()
        serializer = self.get_serializer(data={'doctor': doctor, 'matching': self.kwargs['matching_id'], **request.data})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def get_queryset(self):
        """
            path variable로 matching_id를 받아 필터링한 쿼리셋을 가져온다.
        """
        matching_id = self.kwargs['matching_id']
        return Review.objects.filter(id=matching_id)

    def get_doctor_id(self):
        """
            matching_id에 해당하는 doctor_id를 return한다.
        """
        matching = Matching.objects.get(id=self.kwargs['matching_id'])
        return matching.package.doctor

class ReadOnlyReviewAPI(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """
            path variable로 doctor의 id를 받아 필터링한 쿼리셋을 가져온다.
        """
        doctor_id = self.kwargs['doctor_id']
        return Review.objects.filter(doctor=doctor_id)

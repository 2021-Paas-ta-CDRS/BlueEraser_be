from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from package.models import Package

from package.serializers import PackageSerializer

class PackageAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'doctor': request.user.doctor, **request.data.dcit()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_queryset(self):
        return Package.objects.filter(doctor=self.request.user.doctor)

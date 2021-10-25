from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from patient.models import Patient
from patient.serializers import PatientSerializer, UpdatePatientSerializer
from user.serializers import CreateUserSerializer, UpdateUserSerializer

class CreatePatientAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'user_type': 'P', **request.data.dict()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UpdatePatientAPI(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdatePatientSerializer
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
        return {'user_id': request.user.id, **request.data.dict()}

class GetPatientAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

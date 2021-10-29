from django.db.models import fields
from rest_framework import serializers
from .models import Certificate, Doctor
from user.serializers import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Doctor
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_details = representation.pop('user')
        representation.update(user_details)
        return representation

class UpdateDoctorSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id')
    class Meta:
        model = Doctor
        fields = ('user_id', 'hospital_address', )
    
    def update_or_create(self):
        validated_data = {**self.validated_data, }
        doctor, _ = Doctor.objects.update_or_create(
            user_id=validated_data.pop('user')['id'],
            defaults=validated_data
        )
        return doctor

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

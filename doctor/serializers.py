from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class UpdateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('user', 'hospital_address', )
        extra_kwargs = {
            'user': {'validators': []},
        }
    
    def update_or_create(self):
        validated_data = {**self.validated_data, }
        doctor, _ = Doctor.objects.update_or_create(
            user=validated_data.pop('user'),
            defaults=validated_data
        )
        return doctor

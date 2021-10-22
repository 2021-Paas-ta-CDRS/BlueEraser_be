from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class UpdateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('hospital_address', )
    
    def create(self, validated_data):
        doctor, created = Doctor.objects.update_or_create(
            user=self.context['request'].user,
            defaults={'hospital_address': validated_data['hospital_address'], }
        )
        return doctor

from rest_framework import serializers
from .models import Doctor
from user.models import User

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

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

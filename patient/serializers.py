from rest_framework import serializers
from .models import Patient
from user.serializers import UserSerializer

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_details = representation.pop('user')
        representation.update(user_details)
        return representation

class UpdatePatientSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id')
    class Meta:
        model = Patient
        fields = ('user_id', 'job', )
    
    def update_or_create(self):
        validated_data = {**self.validated_data, }
        patient, _ = Patient.objects.update_or_create(
            user_id=validated_data.pop('user')['id'],
            defaults=validated_data
        )
        return patient

from rest_framework import serializers
from .models import Patient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class UpdatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('job', )
    
    def create(self, validated_data):
        patient, created = Patient.objects.update_or_create(
            user=self.context['request'].user,
            defaults={'job': validated_data['job'], }
        )
        return patient

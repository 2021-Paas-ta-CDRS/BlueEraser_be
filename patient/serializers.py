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
    
    def update(self, instance, validated_data):
        patient, _ = Patient.objects.update_or_create(
            user=instance,
            defaults={'job': validated_data['job'], }
        )

        return patient

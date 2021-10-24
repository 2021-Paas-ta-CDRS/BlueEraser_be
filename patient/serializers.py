from rest_framework import serializers
from .models import Patient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class UpdatePatientSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id')
    class Meta:
        model = Patient
        fields = ('user_id', 'job', )
    
    def update_or_create(self):
        validated_data = {**self.validated_data, }
        patient, _ = Patient.objects.update_or_create(
            user=validated_data.pop('user')['id'],
            defaults=validated_data
        )
        return patient

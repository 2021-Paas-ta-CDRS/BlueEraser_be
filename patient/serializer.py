from rest_framework import serializers
from patient.models import Patient
from user.models import User
from user.serializers import UserSerializer

class CreatePatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Patient
        fields = ('user', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(email=validated_data['user']['email'], password=validated_data['user']['password'])
        patient = Patient.objects.create(user=user)
        
        return patient

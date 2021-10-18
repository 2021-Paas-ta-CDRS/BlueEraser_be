from rest_framework import serializers
from user.models import User

class CreatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            user_type = 'P',
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user

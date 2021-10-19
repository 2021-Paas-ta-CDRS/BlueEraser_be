from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            user_type = validated_data['user_type'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user

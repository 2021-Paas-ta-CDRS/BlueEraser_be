from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'age', 'phone_number', 'ssn', 'sex', 'address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            name = validated_data['name'],
            age = validated_data['age'],
            phone_number = validated_data['phone_number'],
            ssn = validated_data['ssn'],
            sex = validated_data['sex'],
            address = validated_data['address'],
        )
        return user

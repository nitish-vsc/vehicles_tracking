from rest_framework import serializers
from .models import RegisterUser


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['name', 'email', 'mobile', 'username']

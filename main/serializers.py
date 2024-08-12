from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name','last_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['password'],
            validated_data['first_name'],
            validated_data['last_name']
        )
        return user

class TurPaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tur_paket
        fields = '__all__'

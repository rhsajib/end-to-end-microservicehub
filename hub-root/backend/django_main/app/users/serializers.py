from rest_framework import serializers
from .models import User

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'mobile', 
            'about', 
            'profile_photo',
        ]

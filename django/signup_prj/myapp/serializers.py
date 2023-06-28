from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser,CustomUserManager

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields="__all__"
        # fields=('id','username','email','password')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields="__all__"
        
class EmailVerifySerializer(serializers.Serializer):
    email= serializers.EmailField()
    otp= serializers.CharField()




              
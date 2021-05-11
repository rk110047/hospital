from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings
from .models import SubUser

import datetime






class RegisterSerializer(serializers.Serializer):
    username                    =   serializers.CharField(max_length=120)
    email                       =   serializers.EmailField()
    password                    =   serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)
    confirm_password            =   serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)








class LoginSerializer(serializers.Serializer):
    username    =   serializers.CharField(max_length=120)
    password    =   serializers.CharField(
        style={'input_type':'password'},
        max_length=128, min_length=6, write_only=True, )


class PasswordChangeSerializer(serializers.Serializer):
    old_password    =   serializers.CharField(
        style={'input_type':'password'},
        max_length=128, min_length=6, write_only=True, )
    new_password    =   serializers.CharField(
        style={'input_type':'password'},
        max_length=128, min_length=6, write_only=True, )


class SubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model       =   SubUser
        fields      =   "__all__"
        read_only_fields    =   ['user']
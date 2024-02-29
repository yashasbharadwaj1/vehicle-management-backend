from .models import User 
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from django.contrib.auth.password_validation import validate_password 
from rest_framework.validators import UniqueValidator 
from vendor.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password','type_of_user') 
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token["type_of_user"] = user.type_of_user 
        token['user_id'] = user.user_id

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'type_of_user')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            type_of_user=validated_data['type_of_user']
        )

        user.set_password(validated_data['password'])
        user.save()
        if validated_data['type_of_user'] == "vendor":
            vendor = Vendor.objects.create(
                name = validated_data['username'],
                details = "vendor details"
            )
            vendor.save()
        return user
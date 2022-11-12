from django.contrib.auth.models import User
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 8,
                "max_length": 255,
            }
        }


class UserInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class UserUpdateSerializer(UserInputSerializer):
    confirm_password = serializers.CharField()

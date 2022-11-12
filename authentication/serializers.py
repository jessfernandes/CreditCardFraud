from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RenovationSerializer(serializers.Serializer):
    tk_renovation = serializers.CharField()

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.vk.views import VKOAuth2Adapter

from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_auth.registration.serializers import SocialLoginSerializer
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken



class GoogleSocialLoginSerializer(SocialLoginSerializer):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier for the UserManager to create a new user.
        return User.objects.create_user(**validated_data)


class VKSocialLoginSerializer(SocialLoginSerializer):
    adapter_class = VKOAuth2Adapter
    client_class = OAuth2Client

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Получаем объект запроса
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier for the UserManager to create a new user.
        return User.objects.create_user(**validated_data)

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



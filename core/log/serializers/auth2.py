from rest_framework import serializers
from .register import *
import os
from rest_framework.exceptions import AuthenticationFailed


# class GoogleSocialAuthSerializer(serializers.Serializer):
#     auth_token = serializers.CharField()
#
#     def validate_auth_token(self, auth_token):
#         user_data = GoogleSocialAuthSerializer.Google.validate(auth_token)
#         try:
#             user_data['sub']
#         except:
#             raise serializers.ValidationError(
#                 'The token is invalid or expired. Please login again.'
#             )
#
#         if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
#
#             raise AuthenticationFailed('oops, who are you?')
#
#         user_id = user_data['sub']
#         email = user_data['email']
#         name = user_data['name']
#         provider = 'google'
#
#         return register_social_user(
#             provider=provider, user_id=user_id, email=email, name=name)


class VKAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=200)
    expires_in = serializers.IntegerField()
    user_id = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class GoogleAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=300)
    expires_in = serializers.IntegerField()
    # user_id = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
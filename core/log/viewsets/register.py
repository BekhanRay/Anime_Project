from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect
from rest_auth.registration.views import SocialLoginView
from rest_framework.permissions import AllowAny

from core.log.serializers import VKAuthSerializer, GoogleAuthSerializer
from core.log.serializers.register import *

from rest_framework import status, request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.vk.views import VKOAuth2Adapter


class GoogleAuthViewSet(ViewSet):
    adapter_class = GoogleOAuth2Adapter
    serializer_class = GoogleAuthSerializer
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000'  # Update with your callback URL

    def extract_access_token_and_code(self, request):
        query_params = request.GET
        access_token = query_params.get('access_token', '')
        code = query_params.get('code', '')
        print(query_params)
        return access_token, code

    @action(detail=True, methods=['post'])
    def get_token(self, request):
        access_token, code = self.extract_access_token_and_code(request)

        # Дальнейшая обработка access_token и code
        # ...
        print(access_token)
        return Response({'access_token': access_token, 'code': code})

    @action(detail=False, methods=['get'])
    def auth(self, request):
        # Redirect the user to the Google authentication page
        client_id = '854288019179-b801qvtn8fqbo6illmgcpfe2vmcj15ft.apps.googleusercontent.com'  # Replace with your Google client ID
        redirect_uri = 'http://127.0.0.1:8000/api/social-google/'  # Replace with your redirect URL
        google_auth_url = f'https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code token&scope=email%20profile'
        return redirect(google_auth_url)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "refresh": res["refresh"],
                "access": res["access"],
            },
            status=status.HTTP_201_CREATED,
        )


class VKAuthViewSet(ViewSet):
    adapter_class = VKOAuth2Adapter
    serializer = VKSocialLoginSerializer(data=request, context={'request': request})
    serializer_class = VKAuthSerializer
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000/api/social-vk/'

    @action(detail=False, methods=['get'])
    def auth(self, request):
        client_id = '51640013'
        redirect_uri = 'http://127.0.0.1:8000/api/social-vk/'
        vk_auth_url = f'https://oauth.vk.com/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&code&scope=email'
        return redirect(vk_auth_url)

    # @action(detail=True, methods=['post'])
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "user": serializer.data,
                "refresh": res["refresh"],
                "access": res["access"],
            },
            status=status.HTTP_201_CREATED,
        )

    # def post(self, request):
    #     return self.create(request)


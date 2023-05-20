from django.template.defaulttags import url
from django.urls import path
from rest_framework import routers

from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.user.viewsets import UserViewSet
from core.anime.viewsets import AnimeViewSet
from core.log.viewsets import VKAuthViewSet, GoogleAuthViewSet # , VKAuthView, GoogleAuthView

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

router.register(r'user', UserViewSet, basename='user')
router.register(r'anime', AnimeViewSet, basename='anime')

router.register(r'social-vk', VKAuthViewSet, basename='social-auth-vk')
router.register(r'social-google', GoogleAuthViewSet, basename='social-auth-google')
#router.register(r'^$', schema_view, basename='swagger')


urlpatterns = [
    *router.urls,
]

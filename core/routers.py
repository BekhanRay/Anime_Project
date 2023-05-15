from rest_framework import routers

from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.user.viewsets import UserViewSet
from core.anime.viewsets import AnimeViewSet


router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

router.register(r'user', UserViewSet, basename='user')
router.register(r'anime', AnimeViewSet, basename='anime')


urlpatterns = [*router.urls]

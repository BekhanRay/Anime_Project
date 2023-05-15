from rest_framework.permissions import IsAuthenticated, AllowAny
from core.anime.models import Anime
from core.anime.serializers import AnimeSerializer
from core.abstract.viewsets import AbstractViewSet


class AnimeViewSet(AbstractViewSet):
    http_method_names = ('post', 'get')
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    serializer_class = AnimeSerializer

    def get_queryset(self):
        return Anime.objects.all()

    def get_object(self):
        obj = Anime.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj
    
from rest_framework import viewsets


class AbstractViewSet(viewsets.ModelViewSet):
    # filter_backends = ['filters.OrderingFilter']
    ordering_fields = ["updated", "created"]
    ordering = ["-updated"]

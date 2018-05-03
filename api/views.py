from django.conf import settings
from rest_framework import (mixins, viewsets)

from .serializers import ConsoleLogSerializer

from consolelogs.models import ConsoleLog


class ConsoleLogViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = ConsoleLogSerializer
    queryset = ConsoleLog.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

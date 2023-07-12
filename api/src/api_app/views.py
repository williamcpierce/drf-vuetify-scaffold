from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class MessageViewSet(ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

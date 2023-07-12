from rest_framework.serializers import ModelSerializer

from . import models


class MessageSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"
        read_only_fields = ["id"]

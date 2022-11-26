from rest_framework.serializers import HyperlinkedModelSerializer

from . import models


class MessageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Message
        fields = [field.name for field in model._meta.fields]
        fields.extend(["id"])

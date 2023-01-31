from rest_framework import serializers

from . import models


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorite
        fields = ["id", "user", "article"]

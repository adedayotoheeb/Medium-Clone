from rest_framework import serializers

from . import models


class RatingSerializer(serializers.ModelSerializer):
    rated_by = serializers.SerializerMethodField(read_only=True, method_name="get_rated_by")
    article = serializers.SerializerMethodField(read_only=True, method_name="get_article")

    class Meta:
        model = models.Rating
        fields = ["id", "article", "rated_by", "value"]

    def get_rated_by(self, obj):
        return obj.rated_by.username

    def get_article(self, obj):
        return obj.article.title
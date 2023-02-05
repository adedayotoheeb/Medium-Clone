from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from . import models

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(method_name="get_created_at", read_only= True)
    updated_at = serializers.SerializerMethodField(method_name="get_updated_at", read_only= True)

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y, %H:%M:%S")
        return formatted_date

    class Meta:
        model = models.Comment
        fields = ["id", "author", "article", "body", "created_at", "updated_at"]


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.user.username")
    article = serializers.ReadOnlyField(source="article.title")
    created_at = serializers.SerializerMethodField(method_name="get_created_at", read_only= True)
    updated_at = serializers.SerializerMethodField(method_name="get_updated_at", read_only= True)

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y, %H:%M:%S")
        return formatted_date

    class Meta:
        model = models.Comment
        fields = ["id", "author", "article", "body", "created_at", "updated_at"]

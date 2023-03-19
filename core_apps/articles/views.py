import logging

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, RetrieveAPIView

from core_apps.articles.models import Article, ArticleViews

from . import exceptions, pagination, serializers
from .filters import ArticleFilter
from .permissions import IsOwnerOrReadOnly
from .renderers import ArticleJSONRenderer, ArticlesJSONRenderer

User = get_user_model()

logger = logging.getLogger(__name__)


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = serializers.ArticleSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Article.objects.all()
    renderer_classes = [ArticlesJSONRenderer]
    pagination_class = pagination.ArticlePagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ArticleFilter
    search_fields =  ['title', 'author']
    ordering_fields = ["created_at", "username"]


class ArticleCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = serializers.ArticleCreateSerializer
    renderer_classes = [ArticleJSONRenderer]

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["author"] = user.pkid
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"article {serializer.data.get('title')} created by {user.username}"
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailView(RetrieveAPIView):
    renderer_classes = [ArticleJSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field =  "slug"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, slug=self.kwargs["slug"])
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        if not ArticleViews.objects.filter(article=article, ip=ip).exists():
            ArticleViews.objects.create(article=article, ip=ip)

            article.views += 1
            article.save()

        serializer = serializers.ArticleSerializer(article, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)
    


class UpdateArticle(UpdateAPIView):
  serializer_class = serializers.ArticleUpdateSerializer
  lookup_field = "slug"
  permission_classes = [permissions.IsAuthenticated]
  
  def put(self, request, *args, **kwargs):
      article = get_object_or_404(Article, slug=self.kwargs["slug"])
      if article is  None:
          raise NotFound("The article doesnt exist in our catalog")
      user = request.user
      if article.author != user:
          raise exceptions.UpdateArticle
      
      serializer = serializers.ArticleUpdateSerializer(article, data=request.data, many=False)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ArticleDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):

        article = self.get_object()

        if article is None:
            raise NotFound("That article does not exist in our catalog")
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Deletion was successful"
        else:
            data["failure"] = "Deletion failed"

        return Response(data=data)

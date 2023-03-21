from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.ArticleListAPIView.as_view(), name="all-articles"),
    path("create/", views.ArticleCreateAPIView.as_view(), name="create-article"),
    path("details/<slug:slug>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("delete/<slug:slug>/", views.ArticleDeleteAPIView.as_view(), name="delete-article"),
    path("update/<slug:slug>/", views.UpdateArticle.as_view(), name="update-article"),
]



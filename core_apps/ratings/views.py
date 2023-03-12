import exceptions
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core_apps.articles import models as article_model


# Create your views here.
class CreateArticleView(APIView):
    permission_classes =  [IsAuthenticated]

    def post(request, article_id):
        author = request.user
        article = get_object_or_404(article_model.Article, article_id)
        data = request.data

        if article.author == author:
            return exceptions.CantRateYourArticle
        
        already_exists = article.article_ratings.filter()
        

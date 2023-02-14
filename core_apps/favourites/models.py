from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import get_object_or_404

from core_apps.articles import models as article_model
from core_apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Favorite(TimeStampedUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    article = models.ForeignKey(
        article_model.Article, on_delete=models.CASCADE, related_name="article_favorites"
    )

    def __str__(self) -> str:
        return f"{self.user.username} favorited {self.article.title}"

    def is_favorited(self, user, article) -> bool:
        article = self.article
        user = self.user
        
        get_object_or_404(models.Article, pkid=article)
        
        queryset = Favorite.objects.filter(article_id=article, user_id=user)

        if queryset:
            return True
        return False

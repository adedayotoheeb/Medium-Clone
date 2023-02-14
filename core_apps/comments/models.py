from django.contrib.auth import get_user_model
from django.db import models

from core_apps.articles import models as article_model
from core_apps.common.models import TimeStampedUUIDModel
from core_apps.profiles import models as profile_model

User = get_user_model()


class Comment(TimeStampedUUIDModel):
    article = models.ForeignKey(
        article_model.Article, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(profile_model.Profile, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.author} commented on {self.article}"

from django.contrib.auth import get_user_model
from django.db import models

from core_apps.articles import models
from core_apps.common.models import TimeStampedUUIDModel
from core_apps.profiles import models

User = get_user_model()


class Comment(TimeStampedUUIDModel):
    article = models.ForeignKey(
        models.Article, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(models.Profile, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.author} commented on {self.article}"

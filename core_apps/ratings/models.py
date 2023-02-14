# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.articles import models as article_model
from core_apps.common.models import TimeStampedUUIDModel

from . import choices

User = get_user_model()


class Rating(TimeStampedUUIDModel):
    article = models.ForeignKey(
       article_model.Article, related_name="article_ratings", on_delete=models.CASCADE
    )
    rated_by = models.ForeignKey(
        User, related_name="user_who_rated", on_delete=models.CASCADE
    )
    value = models.IntegerField(
        verbose_name=_("rating value"),
        choices=choices.RATINGS_RANGE,
        default=0,
        help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
    )
    review = models.TextField(verbose_name=_("rating review"), blank=True)

    class Meta:
        unique_together = ["rated_by", "article"]

    def __str__(self):
        return f"{self.article.title} rated at {self.value}"

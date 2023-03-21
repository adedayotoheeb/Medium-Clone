from django.db import models
from django.utils.translation import gettext_lazy as _


class Reactions(models.IntegerChoices):
        LIKE = 1, _("like")
        DISLIKE = -1, _("dislike")
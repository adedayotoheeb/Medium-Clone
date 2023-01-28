from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name:str = 'core_apps.articles'
    verbose_name: str = _("Articles")

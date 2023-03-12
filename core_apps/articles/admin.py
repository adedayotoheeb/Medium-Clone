from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Article)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "author", "slug", "article_read_time", "views"]
    list_display_links = ["pkid", "author"]
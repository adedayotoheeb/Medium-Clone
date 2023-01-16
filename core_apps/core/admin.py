from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
# Register your models here.


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    pass

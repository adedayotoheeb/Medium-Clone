from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from . import models
from core_apps.core import forms
# Register your models here.


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_form = forms.UserCreationForm
    ordering = ['email']
    form = forms.UserChangeForm
    model = models.User
    list_display = [
        "pkid",
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    list_display_links = ['id','pkid', 'email']
    list_filter = ["email", "username"]
    search_fields = ["email__istartswith", "username__istartswith", "first_name__istartswith", "last_name__istartswith"]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {"fields": ("username", "first_name", "last_name")},
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )


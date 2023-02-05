from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "core_apps.profiles"

router = routers.SimpleRouter()
router.register('', views.ProfilesViewSet, basename='profile')


urlpatterns = router.urls

"""medium_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from drf_yasg import views, openapi
from rest_framework import permissions

admin.site.site_header = 'Medium Clone Admin'
admin.site.index_title = 'Medium Clone Admin Portal'
admin.site.site_title = "Welcome to Medium Clone API Portal"

schema_view = views.get_schema_view(
    openapi.Info(   
      title="Medium Clone API",
        default_version="v1",
        description="API endpoints for the Medium Clone Application",
        contact=openapi.Contact(email="adedayotoheeb@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/v1/auth", include('djoser.urls')),
    path("api/v1/auth", include('djoser.urls.jwt')),
]

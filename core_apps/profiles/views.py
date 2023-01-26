from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from . import renderers
from . import models
from . import serializers

# Create your views here.


class ProfilesViewSet(ModelViewSet):
    http_method_names = ['get','put']
    # permission_classes = [permissions.IsAuthenticated]
    renderer_classes= [renderers.ProfilesJSONRenderer]
    queryset = models.Profile.objects.select_related('user')
    lookup_field = 'user__username'

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.ProfilesSerializer
        elif self.request.method == "PUT":
            return serializers.UpdateProfileSerializer



  

    
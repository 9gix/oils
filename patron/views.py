from django.shortcuts import render
from django.contrib.auth import models as auth_models
from rest_framework import viewsets

from . import models
from . import serializers
from . import filters

# Create your views here.

class PatronViewSet(viewsets.ModelViewSet):
    queryset = models.Patron.objects.all()
    serializer_class = serializers.PatronSerializer
    filter_class = filters.PatronFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer

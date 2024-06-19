from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from blog.models import *
from blog.serializer import *


# Create your views here.


class RobotsViewSet(viewsets.ModelViewSet):
    queryset = Robots.objects.all()
    serializer_class = RobotsSerializer
    permission_classes = [AllowAny]







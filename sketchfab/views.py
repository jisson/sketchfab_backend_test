import logging

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from sketchfab.models import Model3d

from sketchfab.serializers import UserSerializer, Model3dSerializer

logger = logging.getLogger('sketchfab')


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)


class Model3dViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Model3d.objects.all()
        serializer = Model3dSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Model3d.objects.all()
        model3d = get_object_or_404(queryset, pk=pk)
        serializer = Model3dSerializer(model3d, context={'request': request})
        return Response(serializer.data)


def index(request):
    return render(request, 'sketchfab/index.html')



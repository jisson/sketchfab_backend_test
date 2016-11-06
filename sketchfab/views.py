import logging

from badgify.models import Badge
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.views.generic import View
from django.conf import settings
from django.contrib import messages

from sketchfab.forms import RegistrationForm
from sketchfab.models import Model3d
from sketchfab.serializers import UserSerializer, Model3dSerializer, BadgeSerializer

logger = logging.getLogger('sketchfab')


class UserViewSet(viewsets.ViewSet):
    """
    Returns a list of all registered users in the system.

    For more details on how accounts are activated please [see here][ref].

    [ref]: http://example.com/activating-accounts
    """

    def list(self, request):
        """
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """

        """
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    @detail_route()
    def badges(self, request, pk=None):
        """
        Returns a list of all badges earned by the given user.
        """
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        awards = user.badges.all()
        return Response([BadgeSerializer(award.badge, context={'request': request}).data for award in awards])




class BadgeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Badge.objects.all()
        serializer = BadgeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Badge.objects.all()
        badge = get_object_or_404(queryset, pk=pk)
        serializer = BadgeSerializer(badge, context={'request': request})
        return Response(serializer.data)


class Model3dViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Model3d.objects.all()
        serializer = Model3dSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Model3d.objects.all()

        model3d = get_object_or_404(queryset, pk=pk)

        hit_count = HitCount.objects.get_for_object(model3d)
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        logger.debug(hit_count_response)

        serializer = Model3dSerializer(model3d, context={'request': request})
        return Response(serializer.data)


def index(request):
    return render(request, 'sketchfab/index.html')


class LoginView(View):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, "You have been logged in successfully!")
            else:
                messages.info(request, "You must activate your account before be able to login.")
        else:
            messages.error(request, "Invalid credentials!")
        return redirect('index')


class LogoutView(View):

    def get(self, request):
        auth_logout(request)
        messages.info(request, "You have been logged out.")
        return redirect('index')


# def register(request):
#
#     if request.method == 'POST':
#         registration_form = RegistrationForm(data=request.POST)
#         if registration_form.is_valid():
#             user = registration_form.save()
#             user = authenticate(username=user.username, password=request.POST['password'])
#             auth_login(request, user)
#             return redirect('index')
#     else:
#         registration_form = RegistrationForm()
#
#     return render(request, 'sketchfab/register.html', {'registration_form': registration_form})

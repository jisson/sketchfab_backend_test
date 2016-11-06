import logging

from badgify.models import Badge
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.views.generic import View
from django.contrib import messages

from sketchfab.models import Model3d
from sketchfab import services as sketchfab_services
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

        model3d = sketchfab_services.get_model_with_hit_count(request, queryset, pk=pk)

        serializer = Model3dSerializer(model3d, context={'request': request})
        return Response(serializer.data)


def badges(request):
    return render(request, 'sketchfab/badges.html')


def see_model3d(request, slug):
    # model3d = get_object_or_404(Model3d, slug=slug)
    #
    # hit_count = HitCount.objects.get_for_object(model3d)
    # hit_count_response = HitCountMixin.hit_count(request, hit_count)

    model3d = sketchfab_services.get_model_with_hit_count(request, Model3d, slug=slug)

    return render(request, 'sketchfab/model3ds.html', context={'model3d': model3d})


def index(request):

    model3d_list = Model3d.objects.all()
    paginator = Paginator(model3d_list, 10)

    page = request.GET.get('page')
    try:
        model3ds = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        model3ds = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        model3ds = paginator.page(paginator.num_pages)

    return render(request, 'sketchfab/index.html', context={'model3ds': model3ds})


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

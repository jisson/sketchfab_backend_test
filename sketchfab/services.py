import logging

from badgify.models.award import Award
from badgify.models.badge import Badge
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from sketchfab.models import Model3d
from sketchfab import utils as sketchfab_utils

__author__ = 'Pierre Rodier | pierre@buffactory.com'

logger = logging.getLogger('sketchfab')


def get_badge_by_slug(slug):
    """
    Retrieve a Badge instance corresponding to given slug.
    Use that method instead of Django orm to ensure your badges has been correctly synced.

    :param slug:    The slug of the Badge instance to retrieve
    :raise          ImproperlyConfigured exception if the asked badge cannot be found.

    :return:        A badgify.models.base.badge object
    """
    try:
        return Badge.objects.get(slug=slug)
    except Badge.DoesNotExist:
        message = "Badge with slug {} does not exists! Maybe you forgot to run the 'badgify_sync' command?".format(slug)
        logger.error(message)
        raise ImproperlyConfigured(message)


def grant_user_with_reward(user, badge_slug):
    """
    Grant the given user with the badge related to 'badge_slug'. That method could be called safely as it won't
    create a new reward if the user already earned it.

    :param user:            User instance to grant
    :param badge_slug:      The slug of the badge to give to the user
    """

    badge = get_badge_by_slug(badge_slug)
    award, created = Award.objects.get_or_create(user=user, badge=badge)
    if created:
        logger.info("Granted user: {0} with badge: {1}".format(user.username, badge.slug))


def get_model_with_hit_count(request, klass, *args, **kwargs):
    """
    Retrieve a model object from the database and update the HitCount related to that object.

    :param request:     The request performed.
    :param klass:       May be a Model, Manager, or QuerySet object.

    All other passed arguments and keyword arguments are used in the get() query.

    :raise Http404: That method is based on django.shortcuts.get_object_or_404 method. So a Http404 exception could
    be raises if the object does not exist.

    :return:    An object matching the query.
    """

    model = get_object_or_404(klass, *args, **kwargs)
    hit_count = HitCount.objects.get_for_object(model)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    logger.debug(hit_count_response)
    return model


def check_pioneer_reward(user):
    """
    Check if the given user has joined for more than a year. If so, the user will be granted with 'pioneer' badge.
    That method must be called during login.

    :param user:    User instance
    """

    date_joined = user.date_joined
    if sketchfab_utils.is_date_timeout(date_joined, timeout=31536000):
        # User is registered for more than a year
        grant_user_with_reward(user, 'pioneer')


def check_star_reward(model3d, hits):
    """
    Check if there is more than 1000 hits on given model3d. If so, the owner of the model3d will be granted with
    'star' badge.

    :param model3d:     A model3d instance
    :param hits:        The number of hits related to that model
    """

    if hits >= 1000:
        user = model3d.user
        grant_user_with_reward(user, 'star')


def check_collector_reward(user):
    """
    Check if the given user uploaded more than 5 model3ds. If so, the user will be granted with the 'collector' badge.

    :param user:        User instance
    """

    # Counting number of model3d uploaded by that user
    count = Model3d.objects.filter(user=user).count()

    # User must be rewarded!
    if count >= 5:
        grant_user_with_reward(user, 'collector')

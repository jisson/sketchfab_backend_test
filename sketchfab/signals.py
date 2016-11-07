import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from hitcount.models import HitCount

from sketchfab.models import Model3d
from sketchfab import services as sketchfab_services

__author__ = 'Pierre Rodier | pierre@buffactory.com'

logger = logging.getLogger('sketchfab')


@receiver(post_save, sender=Model3d)
def check_if_user_earned_collector_reward(sender, instance, created, **kwargs):
    """
    That method handle post_save signal from Model3d and check if a reward must be
    granted to the owner of the Model3d.
    """

    logger.debug("check_if_user_earned_collector_reward raised")
    if created:
        user = instance.user
        sketchfab_services.check_collector_reward(user)


@receiver(post_save, sender=HitCount)
def check_if_user_earned_star_reward(sender, instance, **kwargs):
    """
    That method handle post_save signal from HitCount and check if a reward must be
    granted to the owner of the Model3d.
    """

    logger.debug("check_if_user_earned_star_reward raised")

    hits = instance.hits
    content_object = instance.content_object
    if type(content_object) is Model3d:
        sketchfab_services.check_star_reward(content_object, hits)


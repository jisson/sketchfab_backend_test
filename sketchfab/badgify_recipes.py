from django.contrib.staticfiles.storage import staticfiles_storage

from badgify.recipe import BaseRecipe
from badgify.models.award import Award
import badgify


class StarRecipe(BaseRecipe):
    """
    One of your 3d model have been seen 1000 times.
    """

    name = 'Star'
    slug = 'star'
    description = 'One of your 3d model have been seen 1000 times.'

    @property
    def image(self):
        return staticfiles_storage.open('sketchfab/img/badges/star.png')

    @property
    def user_ids(self):
        return Award.objects.filter(badge=self).values_list('user__id', flat=True)
        # return (User.objects.filter(star=True)
        #         .values_list('id', flat=True))


class CollectorRecipe(BaseRecipe):
    """
    You have uploaded more than 5 3d models.
    """

    name = 'Collector'
    slug = 'collector'
    description = 'You have uploaded more than 5 3d models.'

    @property
    def image(self):
        return staticfiles_storage.open('sketchfab/img/badges/collector.png')

    @property
    def user_ids(self):
        return Award.objects.filter(badge=self).values_list('user__id', flat=True)
        # return (User.objects.filter(star=True)
        #         .values_list('id', flat=True))


class PioneerRecipe(BaseRecipe):
    """
    You have been registered on Sketchfab for more than 1 year.
    """

    name = 'Pioneer'
    slug = 'pioneer'
    description = 'You have been registered on Sketchfab for more than 1 year.'

    @property
    def image(self):
        return staticfiles_storage.open('sketchfab/img/badges/pioneer.png')

    @property
    def user_ids(self):
        return Award.objects.filter(badge=self).values_list('user__id', flat=True)
        # return (User.objects.filter(pioneer=True)
        #         .values_list('id', flat=True))


badgify.register([
    StarRecipe,
    CollectorRecipe,
    PioneerRecipe,
])

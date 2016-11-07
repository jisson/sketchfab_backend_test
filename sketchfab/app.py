from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy as _

__author__ = 'Pierre Rodier | pierre@buffactory.com'


class SketchfabConfig(AppConfig):

    name = 'sketchfab'
    verbose_name = _('sketchfab')

    def ready(self):
        import sketchfab.signals
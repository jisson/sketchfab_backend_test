from django.conf import settings

__author__ = 'Pierre Rodier | pierre@buffactory.com'


PICTURE_MEDIA_PATH = getattr(settings, 'SKETCHFAB_PICTURE_MEDIA_PATH', 'upload/pictures')

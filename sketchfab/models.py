import uuid

from django.db import models
from django.contrib.auth.models import User

import sketchfab.sketchfab_settings as settings
import os


def get_picture_file_path(instance, filename):
    """
    Retrieve file_path for a new picture upload.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(settings.PICTURE_MEDIA_PATH, filename)


class Model3d(models.Model):
    """
    Represents a 3d Model in Sketchfab.
    """
    user = models.ForeignKey(User, related_name='model3ds')

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    description = models.TextField(blank=True)

    picture = models.ImageField(upload_to=get_picture_file_path, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.name

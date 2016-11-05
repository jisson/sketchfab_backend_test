from django.db import models


class Model3d(models.Model):
    """
    Represents a 3d Model in Sketchfab.
    """

    name = models.CharField(max_length=25)

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True)

    # Badges
    # badges


class Model3d(models.Model):
    """
    Represents a 3d Model in Sketchfab.
    """

    name = models.CharField(max_length=25)

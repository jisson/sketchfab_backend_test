# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sketchfab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model3d',
            name='user',
            field=models.ForeignKey(related_name='model3ds', to=settings.AUTH_USER_MODEL),
        ),
    ]

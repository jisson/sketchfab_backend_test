# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import sketchfab.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Model3d',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(null=True, upload_to=sketchfab.models.get_picture_file_path, blank=True)),
                ('name', models.CharField(max_length=25)),
                ('user', models.ForeignKey(related_name='three_d_models', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sketchfab', '0002_auto_20161106_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='model3d',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 11, 6, 13, 24, 19, 301115, tzinfo=utc), unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='model3d',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

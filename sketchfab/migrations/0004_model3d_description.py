# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketchfab', '0003_auto_20161106_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='model3d',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

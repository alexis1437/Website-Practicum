# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]

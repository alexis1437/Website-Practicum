# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20190407_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.TextField(blank=True),
        ),
    ]

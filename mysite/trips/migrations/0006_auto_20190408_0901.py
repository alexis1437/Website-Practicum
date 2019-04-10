# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20190408_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='passenger',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

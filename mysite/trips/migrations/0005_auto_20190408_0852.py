# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('passenger', models.PositiveIntegerField(verbose_name='#_of_passenger', default=0)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.TextField(blank=True, default='Anonymous'),
        ),
    ]

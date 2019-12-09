# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-26 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_place_recommend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='location',
        ),
        migrations.AddField(
            model_name='place',
            name='city',
            field=models.CharField(default='city', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='state',
            field=models.CharField(default='state', max_length=60),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-13 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_auto_20190926_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mediamanager', '0010_auto_20170407_1939'),
    ]

    operations = [
        migrations.AddField(
                model_name='webassettemplate',
                name='data_support',
                field=models.BooleanField(default=False),
        ),
    ]

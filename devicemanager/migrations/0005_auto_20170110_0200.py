# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 20:30
from __future__ import unicode_literals

import storages.backends.s3boto
from django.db import migrations, models

import devicemanager.models


class Migration(migrations.Migration):
    dependencies = [
        ('devicemanager', '0004_auto_20160919_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicegroup',
            name='display_date_time',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appbuild',
            name='app_build',
            field=models.FileField(help_text='The app APK file.',
                                   storage=storages.backends.s3boto.S3BotoStorage(),
                                   upload_to=devicemanager.models.build_upload_location),
        ),
    ]

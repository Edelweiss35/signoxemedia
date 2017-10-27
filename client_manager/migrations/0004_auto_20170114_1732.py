# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('client_manager', '0003_auto_20170114_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='device_logo',
            field=models.ImageField(blank=True,
                                    help_text='A logo of the client for use on the device. If no device logo is provided, the main logo will be used.',
                                    null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='display_device_logo',
            field=models.BooleanField(default=True,
                                      help_text='Whether a logo should be shown on the device or not.'),
        ),
    ]

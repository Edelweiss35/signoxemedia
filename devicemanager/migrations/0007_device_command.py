# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('devicemanager', '0006_auto_20170116_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='command',
            field=models.CharField(blank=True, choices=[('reboot', 'Reboot Device'),
                                                        ('free-space', 'Delete Unused Media'),
                                                        ('clear-media', 'Clear All Device Media'),
                                                        ('reset-device', 'Reset Device')],
                                   max_length=20, null=True),
        ),
    ]

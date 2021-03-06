# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 09:59
from __future__ import unicode_literals

import django.db.models.deletion
import storages.backends.s3boto
from django.db import migrations, models

import devicemanager.models


class Migration(migrations.Migration):
    dependencies = [
        ('devicemanager', '0008_auto_20170419_1218'),
    ]

    operations = [
        migrations.CreateModel(
                name='DeviceScreenShot',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                            verbose_name='ID')),
                    ('image', models.ImageField(
                            storage=storages.backends.s3boto.S3BotoStorage(),
                            upload_to=devicemanager.models.screenshot_upload_location)),
                    ('timestamp', models.DateTimeField(auto_now_add=True)),
                ],
        ),
        migrations.AlterField(
                model_name='device',
                name='command',
                field=models.CharField(blank=True, choices=[('reboot', 'Reboot Device'),
                                                            ('free-space', 'Delete Unused Media'), (
                                                                'clear-media',
                                                                'Clear All Device Media'),
                                                            ('reset-device', 'Reset Device'), (
                                                                'change-realm:dev',
                                                                'Device Realm: development'), (
                                                                'change-realm:stage',
                                                                'Device Realm: staging'), (
                                                                'change-realm:live',
                                                                'Device Realm: live')],
                                       max_length=20,
                                       null=True),
        ),
        migrations.AddField(
                model_name='devicescreenshot',
                name='device',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                        to='devicemanager.Device'),
        ),
    ]

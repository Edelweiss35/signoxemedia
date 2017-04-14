# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('feedmanager', '0008_auto_20170315_1917'),
    ]

    operations = [
        migrations.AlterField(
                model_name='category',
                name='type',
                field=models.CharField(choices=[('RANDOM', 'Random'), ('DATED', 'Dated')],
                                       help_text='Select whether this option is time-sensitive or not.For a time-sensitive category (e.g. "This day in history"), only content relevant to the current date will be fetched.',
                                       max_length=10),
        ),
    ]

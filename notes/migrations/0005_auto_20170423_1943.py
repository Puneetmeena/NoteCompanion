# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 14:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20170423_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_logo',
            field=models.FileField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

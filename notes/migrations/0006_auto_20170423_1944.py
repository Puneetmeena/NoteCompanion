# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20170423_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_logo',
            field=models.FileField(upload_to=''),
        ),
    ]

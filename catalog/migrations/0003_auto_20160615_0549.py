# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160615_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='role',
            name='label',
            field=models.CharField(max_length=50),
        ),
    ]

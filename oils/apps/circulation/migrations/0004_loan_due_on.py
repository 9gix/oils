# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-10 20:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0003_loan_patron'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='due_on',
            field=models.DateField(default=datetime.datetime(2016, 10, 10, 20, 31, 4, 589197, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

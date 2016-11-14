# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-23 07:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_on', models.DateField(blank=True, null=True)),
                ('expire_on', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=12)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('note', models.TextField(blank=True, help_text='Extra Information for Administrator')),
                ('notification_type', models.PositiveSmallIntegerField(default=0)),
                ('loan_duration', models.IntegerField(default=15)),
                ('loan_limit', models.IntegerField(default=2)),
                ('renewal_limit', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='PatronIdentification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=60)),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.IdentificationType')),
                ('patron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identifications', to='account.Patron')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='membership_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.MembershipType'),
        ),
        migrations.AddField(
            model_name='membership',
            name='patron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Patron'),
        ),
    ]

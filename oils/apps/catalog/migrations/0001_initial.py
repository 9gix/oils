# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-23 07:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth', models.SmallIntegerField(blank=True, null=True)),
                ('death', models.SmallIntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgentAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='AgentIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='AgentIdentifierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Agent')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_value', models.CharField(max_length=16)),
                ('raw_json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('place', models.CharField(blank=True, max_length=150)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.Subject')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UniversalIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='UniversalIdentifierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='universalidentifier',
            name='id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.UniversalIdentifierType'),
        ),
        migrations.AddField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Publisher'),
        ),
        migrations.AddField(
            model_name='openlibrary',
            name='id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.UniversalIdentifierType'),
        ),
        migrations.AddField(
            model_name='openlibrary',
            name='oils_book',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Book'),
        ),
        migrations.AddField(
            model_name='classification',
            name='classification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ClassificationType'),
        ),
        migrations.AddField(
            model_name='bookidentifier',
            name='identifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.UniversalIdentifier'),
        ),
        migrations.AddField(
            model_name='bookagent',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Role'),
        ),
        migrations.AddField(
            model_name='book',
            name='agents',
            field=models.ManyToManyField(blank=True, through='catalog.BookAgent', to='catalog.Agent'),
        ),
        migrations.AddField(
            model_name='book',
            name='classifications',
            field=models.ManyToManyField(blank=True, to='catalog.Classification'),
        ),
        migrations.AddField(
            model_name='book',
            name='identifiers',
            field=models.ManyToManyField(related_name='books', through='catalog.BookIdentifier', to='catalog.UniversalIdentifier'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishers',
            field=models.ManyToManyField(blank=True, through='catalog.Publication', to='catalog.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='catalog.Subject'),
        ),
        migrations.AddField(
            model_name='agentidentifier',
            name='id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.AgentIdentifierType'),
        ),
        migrations.AddField(
            model_name='agent',
            name='identifiers',
            field=models.ManyToManyField(blank=True, to='catalog.AgentIdentifier'),
        ),
        migrations.AlterUniqueTogether(
            name='universalidentifier',
            unique_together=set([('id_type', 'value')]),
        ),
        migrations.AlterUniqueTogether(
            name='classification',
            unique_together=set([('classification_type', 'value')]),
        ),
        migrations.AlterUniqueTogether(
            name='agentidentifier',
            unique_together=set([('id_type', 'value')]),
        ),
    ]

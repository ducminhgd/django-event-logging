# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventLoggingModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'NotSet'), (20, 'Info'), (30, 'Warning'), (10, 'Debug'), (40, 'Error'), (50, 'Fatal')], db_index=True, default=20)),
                ('actor', models.CharField(max_length=30)),
                ('action', models.PositiveSmallIntegerField(null=True)),
                ('target', models.CharField(max_length=100, null=True)),
                ('payload', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_logging',
            },
        ),
    ]

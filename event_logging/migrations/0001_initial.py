# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventSourcing',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('actor', models.CharField(max_length=30)),
                ('action', models.PositiveSmallIntegerField(null=True)),
                ('init_params', models.TextField()),
                ('uptd_params', models.TextField()),
                ('status', models.PositiveSmallIntegerField(null=True)),
                ('action_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
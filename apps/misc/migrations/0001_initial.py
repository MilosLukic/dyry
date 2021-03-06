# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(max_length=255)),
                ('discrete', models.BooleanField(default=False)),
                ('units', models.CharField(max_length=255)),
            ],
        ),
    ]

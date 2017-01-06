# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-06 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('origin_street_number', models.CharField(blank=True, max_length=10, null=True)),
                ('origin_street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('origin_city', models.CharField(blank=True, max_length=50, null=True)),
                ('origin_country', models.CharField(blank=True, max_length=40, null=True)),
                ('origin_post_code', models.CharField(blank=True, max_length=5, null=True)),
                ('destination_street_number', models.CharField(blank=True, max_length=10, null=True)),
                ('destination_street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('destination_city', models.CharField(blank=True, max_length=50, null=True)),
                ('destination_country', models.CharField(blank=True, max_length=40, null=True)),
                ('destination_post_code', models.CharField(blank=True, max_length=5, null=True)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('leaving_time', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'verbose_name': 'Trip',
            },
        ),
    ]

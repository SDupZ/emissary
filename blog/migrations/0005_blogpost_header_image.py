# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-08 02:58
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('blog', '0004_auto_20170108_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='header_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_header_image', to='filer.Image'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-06 03:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='created',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='modified',
        ),
    ]
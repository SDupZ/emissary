# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-20 02:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0009_homepagesettings_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagesettings',
            name='services_image_one',
        ),
        migrations.RemoveField(
            model_name='homepagesettings',
            name='services_image_three',
        ),
        migrations.RemoveField(
            model_name='homepagesettings',
            name='services_image_two',
        ),
    ]

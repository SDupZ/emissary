# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-15 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faqpagesettings',
            old_name='article',
            new_name='faq',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-15 21:23
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_auto_20161215_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqitem',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
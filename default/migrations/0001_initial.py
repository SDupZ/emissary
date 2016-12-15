# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-15 21:18
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'FAQ Item',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-08 01:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Blog Post',
            },
        ),
    ]
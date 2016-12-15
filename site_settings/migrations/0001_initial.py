# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-15 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQPageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(blank=True, help_text=b'Something', null=True, on_delete=django.db.models.deletion.CASCADE, to='default.FAQItem')),
            ],
            options={
                'verbose_name': 'FAQ Page Settings',
                'verbose_name_plural': 'FAQ Page Settings',
            },
        ),
    ]

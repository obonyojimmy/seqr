# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-12 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_auto_20170624_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='short_description',
            field=models.TextField(blank=True, default=b''),
        ),
    ]

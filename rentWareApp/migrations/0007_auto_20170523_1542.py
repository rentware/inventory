# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-23 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentWareApp', '0006_rate_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]

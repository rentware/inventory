# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-23 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentWareApp', '0008_auto_20170523_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='amount',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-24 11:40
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('rentWareApp', '0008_auto_20170424_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imagefile',
            field=stdimage.models.StdImageField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
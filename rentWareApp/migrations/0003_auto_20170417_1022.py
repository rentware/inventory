# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-17 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentWareApp', '0002_auto_20170416_1734'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TypeAddress',
            new_name='AddressType',
        ),
        migrations.AddField(
            model_name='address',
            name='address_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentWareApp.AddressType'),
        ),
    ]
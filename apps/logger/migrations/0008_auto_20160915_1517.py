# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-15 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0007_auto_20160915_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='slug',
            field=models.CharField(choices=[('electricity-used', 'electricity-used'), ('electricity-delivered', 'electricity-delivered'), ('gas', 'gas')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='metertariff',
            name='unit',
            field=models.CharField(choices=[('kWh', 'kWh'), ('m3', 'm3')], max_length=10),
        ),
    ]

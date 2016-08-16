# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-15 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityDeliveredReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(db_index=True)),
                ('value_increment', models.DecimalField(decimal_places=3, max_digits=8)),
                ('value_total', models.DecimalField(decimal_places=3, max_digits=9)),
                ('costs', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
                ('tariff', models.PositiveSmallIntegerField(db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElectricityUsedReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(db_index=True)),
                ('value_increment', models.DecimalField(decimal_places=3, max_digits=8)),
                ('value_total', models.DecimalField(decimal_places=3, max_digits=9)),
                ('costs', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
                ('tariff', models.PositiveSmallIntegerField(db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GasReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(db_index=True)),
                ('value_increment', models.DecimalField(decimal_places=3, max_digits=8)),
                ('value_total', models.DecimalField(decimal_places=3, max_digits=9)),
                ('costs', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterIndexTogether(
            name='electricityusedreading',
            index_together=set([('tariff', 'datetime')]),
        ),
        migrations.AlterIndexTogether(
            name='electricitydeliveredreading',
            index_together=set([('tariff', 'datetime')]),
        ),
    ]

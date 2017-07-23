# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnergyUse_time', models.DateTimeField()),
                ('EnergyUse_consumption', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_time', models.DateTimeField()),
                ('summary_use', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_area', models.CharField(max_length=2)),
                ('user_tariff', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='energyuse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.User'),
        ),
    ]
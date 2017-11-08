# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0002_auto_20171108_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='attend',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attend.CurrentWeek'),
        ),
    ]

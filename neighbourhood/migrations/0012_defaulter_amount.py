# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-05 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0011_auto_20200201_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaulter',
            name='amount',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
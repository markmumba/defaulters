# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-24 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0012_defaulter_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='priority',
        ),
        migrations.AddField(
            model_name='defaulter',
            name='Next_Of_Kin_Relationship',
            field=models.CharField(choices=[('Wife', 'Wife'), ('Husband', 'Husband'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Mother', 'Mother'), ('Father', 'Father'), ('Other', 'Other')], default='Wife', max_length=15),
        ),
    ]

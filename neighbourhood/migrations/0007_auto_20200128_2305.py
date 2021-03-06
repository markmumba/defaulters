# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-28 20:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhood', '0006_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='defaulter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('id_number', models.CharField(max_length=12)),
                ('image', models.ImageField(upload_to='post/')),
                ('phone_number', models.CharField(max_length=12)),
                ('post', tinymce.models.HTMLField()),
                ('n_o_k_name', models.CharField(max_length=150)),
                ('n_o_k_phone_number', models.CharField(max_length=12)),
                ('post_date', models.DateTimeField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('email_address', models.EmailField(max_length=254)),
                ('house', models.ManyToManyField(to='neighbourhood.Business')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='username',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.defaulter'),
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]

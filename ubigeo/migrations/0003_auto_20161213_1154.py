# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ubigeo', '0002_auto_20161213_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='centropoblado',
            name='acceso',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='centropoblado',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departamento',
            name='acceso',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='departamento',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distrito',
            name='acceso',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='distrito',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provincia',
            name='acceso',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='provincia',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

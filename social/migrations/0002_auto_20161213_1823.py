# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubigeo', '0006_auto_20161213_1608'),
        ('item', '0002_auto_20161213_1751'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='centrotrabajo',
            unique_together=set([('centro_poblado', 'tipo_centro_trabajo')]),
        ),
    ]

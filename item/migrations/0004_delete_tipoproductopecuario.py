# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_tipoproductopecuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoProductoPecuario',
        ),
    ]
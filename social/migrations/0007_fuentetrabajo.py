# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 12:47
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubigeo', '0001_initial'),
        ('social', '0006_auto_20161215_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuenteTrabajo',
            fields=[
                ('centro_poblado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ubigeo.CentroPoblado', verbose_name='Centro poblado')),
                ('casa_dep', models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en su casa', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Porcentaje')),
                ('campo_dep', models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en el campo', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Porcentaje')),
                ('independiente_dep', models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan de forma independiente', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Porcentaje')),
                ('publico_dep', models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en el sector público', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Porcentaje')),
                ('privado_dep', models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en el sector privado', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Porcentaje')),
                ('total_dep', models.PositiveIntegerField(help_text='Porcentaje total', verbose_name='Total')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 12:56
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_fuentetrabajo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuentetrabajo',
            name='total_dep',
        ),
        migrations.AlterField(
            model_name='fuentetrabajo',
            name='campo_dep',
            field=models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en el campo', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Campo'),
        ),
        migrations.AlterField(
            model_name='fuentetrabajo',
            name='casa_dep',
            field=models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en su casa', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Casa'),
        ),
        migrations.AlterField(
            model_name='fuentetrabajo',
            name='independiente_dep',
            field=models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan de forma independiente', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Independiente'),
        ),
        migrations.AlterField(
            model_name='fuentetrabajo',
            name='privado_dep',
            field=models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en el sector privado', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Sector Privado'),
        ),
        migrations.AlterField(
            model_name='fuentetrabajo',
            name='publico_dep',
            field=models.DecimalField(decimal_places=2, help_text='Porcentaje de habitantes que trabajan en el sector público', max_digits=5, validators=(django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))), verbose_name='Sector Público'),
        ),
    ]
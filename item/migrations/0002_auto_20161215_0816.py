# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProductoAgricola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del producto agricola', max_length=50, verbose_name='Nombre')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tipo de producto agricola',
                'verbose_name_plural': 'tipos de producto agricola',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='TipoProductoDestino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del destino del producto', max_length=50, verbose_name='Nombre')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tipo de destino de producto',
                'verbose_name_plural': 'tipos de destino de producto',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='TipoUnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la unidad de medida', max_length=50, verbose_name='Nombre')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tipo de unidad de medida',
                'verbose_name_plural': 'tipos de unidades de medida',
                'ordering': ('nombre',),
            },
        ),
        migrations.AlterModelOptions(
            name='tipocentrotrabajo',
            options={'ordering': ('nombre',), 'verbose_name': 'tipo centro de trabajo', 'verbose_name_plural': 'tipos de centro de trabajo'},
        ),
        migrations.AlterModelOptions(
            name='tipooficio',
            options={'ordering': ('nombre',), 'verbose_name': 'tipo de oficio', 'verbose_name_plural': 'tipos de oficio'},
        ),
    ]
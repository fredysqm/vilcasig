# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubigeo', '0002_auto_20161220_1054'),
        ('social', '0010_auto_20161220_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pecuario',
            fields=[
                ('centro_poblado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ubigeo.CentroPoblado', verbose_name='Centro poblado')),
                ('n_aves', models.PositiveIntegerField(help_text='Nro de aves producidas por año', verbose_name='Aves')),
                ('n_cuyes', models.PositiveIntegerField(help_text='Nro de cuyes producidos por año', verbose_name='Cuyes')),
                ('n_ovejas', models.PositiveIntegerField(help_text='Nro de ovejas producias por año', verbose_name='Ovejas')),
                ('n_porcinos', models.PositiveIntegerField(help_text='Nro de porcinos producidos por año', verbose_name='Porcinos')),
                ('n_vacunos', models.PositiveIntegerField(help_text='Nro de porcinos producidos por año', verbose_name='Vacunos')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'producto pecuario',
                'verbose_name_plural': 'productos pecuarios',
            },
        ),
        migrations.AlterModelOptions(
            name='oficio',
            options={'verbose_name': 'oficio', 'verbose_name_plural': 'oficios'},
        ),
    ]
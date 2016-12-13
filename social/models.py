from django.contrib.gis.db import models
from ubigeo.models import CentroPoblado



class Ingreso(models.Model):

    centro_poblado = models.OneToOneField(
            CentroPoblado,
            primary_key=True,
            verbose_name='Centro poblado',
        )

    nro_habitantes = models.PositiveIntegerField(
            verbose_name='Nro de habitantes',
            help_text='Total nro de habitantes del centro poblado'
        )

    nro_familias = models.PositiveIntegerField(
            verbose_name='Nro de familias',
            help_text='Total nro de familias del centro poblado'
        )

    m200 = models.PositiveIntegerField(
            verbose_name='Igual ó menor a 200 Soles',
            help_text='Nro de familias con ingresos económicos iguales o menores a 200 Soles al mes'
        )

    m201_499 =  models.PositiveIntegerField(
            verbose_name='De 201 a 499 Soles',
            help_text='Nro de familias con ingresos económicos de 201 a 499 Soles al mes'
        )

    m501_999 =  models.PositiveIntegerField(
            verbose_name='De 500 a 999 Soles',
            help_text='Nro de familias con ingresos económicos de 500 a 999 Soles al mes'
        )

    m1000 = models.PositiveIntegerField(
            verbose_name='Igual ó mayor a 1000 Soles',
            help_text='Nro de familias con ingresos económicos iguales o mayores a 1000 Soles al mes'
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return "%s" % (self.centro_poblado.nombre)

    def save(self, *args, **kwargs):
        self.nro_familias = self.m200 + self.m201_499 + self.m501_999 + self.m1000
        super(Ingreso, self).save(*args, **kwargs)
from django.contrib.gis.db import models
from django.core import validators
from ubigeo.models import CentroPoblado
from item.models import TipoCentroTrabajo, TipoOficio
from decimal import Decimal



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



class CentroTrabajo(models.Model):

    centro_poblado = models.ForeignKey(
            CentroPoblado,
            verbose_name='Centro poblado',
        )

    tipo_centro_trabajo = models.ForeignKey(
            TipoCentroTrabajo,
            verbose_name='Centro de labor',
            help_text='Tipo de centro de trabajo',
        )

    porcentaje = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            verbose_name='Porcentaje',
            help_text='Porcentaje de habitantes que laboran en el centro de trabajo',
            validators=(
                    validators.MinValueValidator(Decimal('0.01')),
                    validators.MaxValueValidator(Decimal('100.00')),
                )
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s (%s)' % (self.tipo_centro_trabajo.nombre, self.porcentaje)

    class Meta:
        unique_together= (('centro_poblado', 'tipo_centro_trabajo'),)
        verbose_name = ('centro de trabajo')
        verbose_name_plural = ('centros de trabajo')



class Oficio(models.Model):

    centro_poblado = models.ForeignKey(
            CentroPoblado,
            verbose_name='Centro poblado',
        )

    tipo_oficio = models.ForeignKey(
            TipoOficio,
            verbose_name='Ocupación',
            help_text='Tipo de ocupación / oficio / profesión',
        )

    porcentaje = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            verbose_name='Porcentaje',
            help_text='Porcentaje de habitantes que ejercen la ocupación / oficio / profesión',
            validators=(
                    validators.MinValueValidator(Decimal('0.01')),
                    validators.MaxValueValidator(Decimal('100.00')),
                )
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s (%s)' % (self.tipo_oficio.nombre, self.porcentaje)

    class Meta:
        unique_together= (('centro_poblado', 'tipo_oficio'),)
        verbose_name = ('Oficio')
        verbose_name_plural = ('Oficios')
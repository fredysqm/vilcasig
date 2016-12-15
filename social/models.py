from django.contrib.gis.db import models
from django.core import validators
from ubigeo.models import CentroPoblado
from item.models import TipoCentroTrabajo, TipoOficio, TipoProductoAgricola, TipoUnidadMedida, TipoProductoDestino, TipoProductoPecuario
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



class Agricola(models.Model):

    centro_poblado = models.ForeignKey(
            CentroPoblado,
            verbose_name='Centro poblado',
        )

    producto = models.ForeignKey(
            TipoProductoAgricola,
            verbose_name='Producto',
            help_text='Tipo de producto agricola',
        )

    cantidad = models.PositiveIntegerField(
            verbose_name='Cantidad',
            help_text='Nro de unidades de producto, producidas por año'
        )

    unidad_medida = models.ForeignKey(
            TipoUnidadMedida,
            verbose_name='Unidad medida',
            help_text='Unidad de medida del producto',
        )

    destino = models.ForeignKey(
            TipoProductoDestino,
            verbose_name='Destino',
            help_text='Destino / finalidad del producto',
        )

    promedio_precio_venta = models.DecimalField(
            max_digits=8,
            decimal_places=2,
            verbose_name='Promedio PV',
            help_text='Promedio de precio de venta del producto',
            validators=(
                    validators.MinValueValidator(Decimal('0')),
                    validators.MaxValueValidator(Decimal('100000.00')),
                )
        )

    promedio_precio_real_venta = models.DecimalField(
            max_digits=8,
            decimal_places=2,
            verbose_name='Promedio PRV',
            help_text='Promedio de precio de venta del producto, en el mercado local',
            validators=(
                    validators.MinValueValidator(Decimal('0')),
                    validators.MaxValueValidator(Decimal('100000.00')),
                )
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s' % (self.producto.nombre,)

    class Meta:
        unique_together= (('centro_poblado', 'producto'),)
        verbose_name = ('producto agricola')
        verbose_name_plural = ('productos agricolas')



class Pecuario(models.Model):

    centro_poblado = models.ForeignKey(
            CentroPoblado,
            verbose_name='Centro poblado',
        )

    producto = models.ForeignKey(
            TipoProductoPecuario,
            verbose_name='Producto',
            help_text='Tipo de producto pecuario',
        )

    cantidad = models.PositiveIntegerField(
            verbose_name='Cantidad',
            help_text='Nro de unidades de producto, producidas por año'
        )

    destino = models.ForeignKey(
            TipoProductoDestino,
            verbose_name='Destino',
            help_text='Destino / finalidad del producto',
        )

    promedio_precio_venta = models.DecimalField(
            max_digits=8,
            decimal_places=2,
            verbose_name='Promedio PV',
            help_text='Promedio de precio de venta por unidad de producto',
            validators=(
                    validators.MinValueValidator(Decimal('0')),
                    validators.MaxValueValidator(Decimal('10000.00')),
                )
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s' % (self.producto.nombre,)

    class Meta:
        unique_together= (('centro_poblado', 'producto'),)
        verbose_name = ('producto pecuario')
        verbose_name_plural = ('productos pecuarios')
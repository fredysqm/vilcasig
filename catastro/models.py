from django.contrib.gis.db import models
from django.core import validators
from ubigeo.models import CentroPoblado



class Sector(models.Model):

    centro_poblado = models.ForeignKey(
                CentroPoblado,
                verbose_name='Centro Poblado',
                help_text='Centro poblado al que pertenece el sector',
            )

    codigo = models.CharField(
                max_length=2,
                verbose_name='Código',
                help_text='Código del sector',
                validators=[
                    validators.RegexValidator(
                        regex='^[0-9]{2}$',
                        message='Debe ingresar dos dígitos.',
                    ),
                ]
            )

    nombre = models.CharField(
                max_length=100,
                verbose_name='Nombre',
                help_text='Nombre del sector',
            )

    geom = models.PolygonField(
                srid=32718,
                verbose_name='Geometría',
                help_text='Geometría asociada al sector, (WKT, EPSG:32718)',
            )

    _centroid = models.PointField(srid=32718,)
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return 'SECTOR: %s (%s), C.P.: %s' % (self.nombre, self.codigo, self.centro_poblado)

    def save(self):
        self.nombre = self.nombre.upper()
        self._centroid = self.geom.centroid
        super(Sector, self).save()

    class Meta:
        verbose_name = ('sector')
        verbose_name_plural = ('sectores')
        ordering = ('codigo',)
        unique_together= (('codigo', 'centro_poblado'),)


class Manzana(models.Model):

    sector = models.ForeignKey(
                Sector,
                verbose_name='Sector',
                help_text='Sector al que pertenece la manzana',
            )

    codigo = models.CharField(
                max_length=3,
                verbose_name='Código',
                help_text='Código de la manzana',
                validators=[
                    validators.RegexValidator(
                        regex='^[0-9]{3}$',
                        message='Debe ingresar tres dígitos.',
                    ),
                ]
            )

    letra = models.CharField(
                max_length=3,
                verbose_name='Letra',
                help_text='Letra de la manzana',
            )

    geom = models.PolygonField(
                srid=32718,
                verbose_name='Geometría',
                help_text='Geometría asociada a la manzana, (WKT, EPSG:32718)',
            )

    _centroid = models.PointField(srid=32718,)
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return 'MANZANA: %s, SECTOR: %s' % (self.codigo, self.sector)

    def save(self):
        self._centroid = self.geom.centroid
        self.letra = self.letra.upper()
        super(Manzana, self).save()

    class Meta:
        ordering = ('codigo',)
        unique_together= (('codigo', 'sector'),)
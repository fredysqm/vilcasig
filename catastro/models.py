from django.contrib.gis.db import models
from ubigeo.models import CentroPoblado



class Perimetro(models.Model):

    centro_poblado = models.OneToOneField(
            CentroPoblado,
            primary_key=True,
            verbose_name='Centro poblado',
        )

    geom = models.PolygonField(
            srid=32718,
            verbose_name='Geometria',
            help_text='Geometria asociada al centro poblado',
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s' % (self.centro_poblado.nombre)
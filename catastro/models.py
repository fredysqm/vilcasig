from django.contrib.gis.db import models
from ubigeo.models import CentroPoblado



class Sector(models.Model):

    codigo = models.CharField(
                max_length=2,
                verbose_name='Código',
                help_text='Código del sector',
            )

    nombre = models.CharField(
                max_length=100,
                verbose_name='Nombre',
                help_text='Nombre del sector',
            )

    centro_poblado = models.ForeignKey(
                CentroPoblado,
                verbose_name='Centro Poblado',
                help_text='Centro poblado al que pertenece el sector',
            )

    creado = models.DateTimeField(auto_now_add=True,)
    modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '(%s) %s' % (self.codigo, self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Sector, self).save()


class Manzana(models.Model):

    codigo = models.CharField(
                max_length=2,
                verbose_name='Código',
                help_text='Código del sector',
            )

    nombre = models.CharField(
                max_length=100,
                verbose_name='Nombre',
                help_text='Nombre del sector',
            )

    centro_poblado = models.ForeignKey(
                CentroPoblado,
                verbose_name='Centro Poblado',
                help_text='Centro poblado al que pertenece el sector',
            )

    creado = models.DateTimeField(auto_now_add=True,)
    modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '(%s) %s' % (self.codigo, self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Sector, self).save()

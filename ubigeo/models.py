from django.contrib.gis.db import models



class Departamento(models.Model):

    codigo = models.CharField(
            primary_key=True,
            max_length=2,
            verbose_name='Ubigeo',
            help_text='Ubigeo según INEI',
        )

    nombre = models.CharField(
            max_length=50,
            verbose_name='Nombre',
            help_text='Nombre del departamento',
        )

    geom = models.MultiPolygonField(
            srid=32718,
            verbose_name='Geometria',
            help_text='Geometria asociada al departamento',
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s' % (self.nombre)



class Provincia(models.Model):

    codigo = models.CharField(
            primary_key=True,
            max_length=4,
            verbose_name='Ubigeo',
            help_text='Ubigeo según INEI',
        )

    departamento = models.ForeignKey(
            Departamento,
            verbose_name='Departamento',
            help_text='Departamento al que pertenece la provincia',
        )

    nombre = models.CharField(
            max_length=100,
            verbose_name='Nombre',
            help_text='Nombre de la provincia',
        )

    geom = models.MultiPolygonField(
            srid=32718,
            verbose_name='Geometria',
            help_text='Geometria asociada a la provincia',
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s, %s' % (self.departamento.nombre, self.nombre)



class Distrito(models.Model):

    codigo = models.CharField(
            primary_key=True,
            max_length=6,
            verbose_name='Ubigeo',
            help_text='Ubigeo según INEI',
        )

    provincia = models.ForeignKey(
            Provincia,
            verbose_name='Provincia',
            help_text='Provincia a la que pertenece el distrito',
        )

    nombre = models.CharField(
            max_length=100,
            verbose_name='Nombre',
            help_text='Nombre del distrito',
        )

    geom = models.MultiPolygonField(
            srid=32718,
            verbose_name='Geometria',
            help_text='Geometria asociada al distrito',
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return '%s, %s' % (self.provincia.nombre, self.nombre)



class CentroPoblado(models.Model):

    codigo = models.CharField(
            primary_key=True,
            max_length=3,
            verbose_name='Código',
            help_text='Código del centro poblado',
        )

    distrito = models.ForeignKey(
            Distrito,
            verbose_name='Distrito',
            help_text='Distrito al que pertenece el centro poblado',
        )

    nombre = models.CharField(
            max_length=100,
            verbose_name='Nombre',
            help_text='Nombre del centro poblado',
        )

    geom = models.MultiPointField(
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
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = ('centro poblado')
        verbose_name_plural = ('centros poblados')
        ordering = ('nombre',)


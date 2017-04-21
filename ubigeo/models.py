from django.contrib.gis.db import models
from django.core import validators



class Departamento(models.Model):

    codigo = models.CharField(
                primary_key=True,
                max_length=2,
                verbose_name='Ubigeo',
                help_text='Ubigeo según INEI',
                validators=[
                    validators.RegexValidator(
                        regex='^[0-9]{2}$',
                        message='Debe ingresar dos dígitos.',
                    ),
                ]
            )

    nombre = models.CharField(
                max_length=50,
                verbose_name='Nombre',
                help_text='Nombre del departamento',
            )

    geom = models.MultiPolygonField(
                srid=32718,
                verbose_name='Geometría',
                help_text='Geometría asociada al departamento, (WKT, EPSG:32718)',
            )

    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '%s' % (self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Departamento, self).save()


class Provincia(models.Model):

    codigo = models.CharField(
                primary_key=True,
                max_length=4,
                verbose_name='Ubigeo',
                help_text='Ubigeo según INEI',
                validators=[
                    validators.RegexValidator(
                        regex='^[0-9]{4}$',
                        message='Debe ingresar cuatro dígitos.',
                    ),
                ]
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
                verbose_name='Geometría',
                help_text='Geometría asociada a la provincia, (WKT, EPSG:32718)',
            )

    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '%s, %s' % (self.departamento.nombre, self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Provincia, self).save()


class Distrito(models.Model):

    codigo = models.CharField(
                primary_key=True,
                max_length=6,
                verbose_name='Ubigeo',
                help_text='Ubigeo según INEI',
                validators=[
                    validators.RegexValidator(
                        regex='^[0-9]{6}$',
                        message='Debe ingresar seis dígitos.',
                    ),
                ]
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
                verbose_name='Geometría',
                help_text='Geometría asociada al distrito, (WKT, EPSG:32718)',
            )

    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '%s, %s' % (self.provincia.nombre, self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Distrito, self).save()


class CentroPoblado(models.Model):

    codigo = models.CharField(
                primary_key=True,
                max_length=3,
                verbose_name='Código',
                help_text='Código del centro poblado',
                validators=[
                    validators.RegexValidator(
                        regex='^[0-9]{3}$',
                        message='Debe ingresar tres dígitos.',
                    ),
                ]
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

    geom = models.PointField(
                srid=32718,
                verbose_name='Geometría',
                help_text='Geometría asociada al centro poblado, (WKT, EPSG:32718)',
            )

    _centroide = models.PointField(srid=32718,)
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '%s' % (self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        self.centroide = self.geom.centroid
        super(CentroPoblado, self).save()

    class Meta:
        verbose_name = ('centro poblado')
        verbose_name_plural = ('centros poblados')
        ordering = ('nombre',)


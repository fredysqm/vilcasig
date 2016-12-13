from django.contrib.gis.db import models



class Departamento(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2, verbose_name='Ubigeo INEI')
    nombre = models.CharField(max_length=50, verbose_name='Nombre departamento')
    geom = models.MultiPolygonField(srid=32718, verbose_name='Geometria')

    def __str__(self):
        return '%s' % (self.nombre)


class Provincia(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4, verbose_name='Ubigeo INEI')
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento')
    nombre = models.CharField(max_length=100, verbose_name='Nombre provincia')
    geom = models.MultiPolygonField(srid=32718, verbose_name='Geometria')

    def __str__(self):
        return '%s, %s' % (self.departamento.nombre, self.nombre)


class Distrito(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6, verbose_name='Ubigeo INEI')
    provincia = models.ForeignKey(Provincia, verbose_name='Provincia')
    nombre = models.CharField(max_length=100, verbose_name='Nombre distrito')
    geom = models.MultiPolygonField(srid=32718, verbose_name='Geometria')

    def __str__(self):
        return '%s, %s' % (self.provincia.nombre, self.nombre)


class CentroPoblado(models.Model):
    codigo = models.CharField(primary_key=True, max_length=3, verbose_name='Código centro poblado')
    distrito = models.ForeignKey(Distrito, verbose_name='Distrito')
    nombre = models.CharField(max_length=100, verbose_name='Nombre centro poblado')
    geom = models.MultiPointField(srid=32718, verbose_name='Geometria')

    def __str__(self):
        return '%s' % (self.nombre)


class Perimetro(models.Model):
    centro_poblado = models.OneToOneField(CentroPoblado, primary_key=True, verbose_name='Centro poblado')
    geom = models.PolygonField(srid=32718, verbose_name='Geometria')

    def __str__(self):
        return '%s' % (self.centro_poblado.nombre)

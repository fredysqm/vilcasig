from django.contrib.gis.db import models


class Departamento(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2,)
    nombre = models.CharField(max_length=50,)
    geom = models.MultiPolygonField(srid=32718,)

    def __str__(self):
        return "%s" % (self.nombre)


class Provincia(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4,)
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=100,)
    geom = models.MultiPolygonField(srid=32718,)

    def __str__(self):
        return "%s, %s" % (self.departamento.nombre, self.nombre)


class Distrito(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6,)
    provincia = models.ForeignKey(Provincia)
    nombre = models.CharField(max_length=100,)
    geom = models.MultiPolygonField(srid=32718,)

    def __str__(self):
        return "%s - %s" % (self.codigo, self.nombre)


class PredioMatriz(models.Model):
    nombre = models.CharField(max_length=50,)
    geom = models.PolygonField(srid=32718,)

    def __str__(self):
        return "%s - %s" % (self.pk, self.nombre)
from django.contrib.gis.db import models



class Oficio(models.Model):

    nombre = models.CharField(
            max_length=50,
            verbose_name='Nombre',
            help_text='Nombre de la ocupación / oficio / profesión'
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return "%s" % (self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Oficio, self).save(*args, **kwargs)



class CentroTrabajo(models.Model):

    nombre = models.CharField(
            max_length=50,
            verbose_name='Nombre',
            help_text='Nombre del centro de trabajo'
        )

    creado = models.DateTimeField(
            auto_now_add=True,
        )

    modificado = models.DateTimeField(
            auto_now=True,
        )

    def __str__(self):
        return "%s" % (self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(CentroTrabajo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ('centro de trabajo')
        verbose_name_plural = ('centros de trabajo')
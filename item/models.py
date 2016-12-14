from django.contrib.gis.db import models



class TipoOficio(models.Model):

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
        super(TipoOficio, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ('tipo de oficio')
        verbose_name_plural = ('tipos de oficio')



class TipoCentroTrabajo(models.Model):

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
        super(TipoCentroTrabajo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ('tipo centro de trabajo')
        verbose_name_plural = ('tipos de centro de trabajo')
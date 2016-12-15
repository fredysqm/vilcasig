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
        ordering = ('nombre',)



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
        ordering = ('nombre',)



class TipoProductoAgricola(models.Model):

    nombre = models.CharField(
            max_length=50,
            verbose_name='Nombre',
            help_text='Nombre del producto agricola'
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
        super(TipoProductoAgricola, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ('tipo de producto agricola')
        verbose_name_plural = ('tipos de producto agricola')
        ordering = ('nombre',)



class TipoUnidadMedida(models.Model):

    nombre = models.CharField(
            max_length=50,
            verbose_name='Nombre',
            help_text='Nombre de la unidad de medida'
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
        super(TipoUnidadMedida, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ('tipo de unidad de medida')
        verbose_name_plural = ('tipos de unidades de medida')
        ordering = ('nombre',)



class TipoProductoDestino(models.Model):

    nombre = models.CharField(
            max_length=50,
            verbose_name='Nombre',
            help_text='Nombre del destino del producto'
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
        super(TipoProductoDestino, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ('tipo de destino de producto')
        verbose_name_plural = ('tipos de destino de producto')
        ordering = ('nombre',)
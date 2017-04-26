from django.db import models
from django.core import validators



TIPO_PERSONA = (
    (1, 'NATURAL'),
    (2, 'JURIDICA'),
)

TIPO_DOCUMENTO = (
    (2, 'DNI'),
    (9, 'RUC'),
    #(1, 'SIN DOCUMENTO'),
)

class Persona(models.Model):

    tipo_persona = models.PositiveSmallIntegerField(choices=TIPO_PERSONA)

    tipo_documento = models.PositiveSmallIntegerField(choices=TIPO_DOCUMENTO)

    nro_documento = models.CharField(
                max_length=11,
                verbose_name='Nro Documento',
                help_text='Nro de documento de la persona',
                validators=[
                    validators.RegexValidator(
                        regex='^[0-9]{8,11}$',
                        message='Debe ingresar un documento válido.',
                    ),
                ]
            )

    nombre = models.CharField(
                max_length=100,
                verbose_name='Nombre',
                help_text='Nombre o razón social',
            )

    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '%s' % (self.nombre,)

    def save(self):
        self.nombre = self.nombre.upper()

        if self.tipo_documento == 2:
            self.tipo_persona = 1
        elif self.tipo_documento == 9:
            self.tipo_persona = 2
        elif self.tipo_documento == 1:
            self.tipo_persona = 1

        super(Persona, self).save()

    class Meta:
        ordering = ('nro_documento',)
        unique_together= (('nro_documento',),)

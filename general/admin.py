from django.contrib import admin
from general.models import Persona



class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_persona', 'tipo_documento', 'nro_documento', 'nombre', '_creado', '_modificado')
    search_fields = ('nombre', 'nro_documento',)
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('tipo_documento', 'nro_documento', 'nombre',)
        }),
    )

admin.site.register(Persona, PersonaAdmin)

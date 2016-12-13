from django.contrib import admin
from item.models import Oficio, CentroTrabajo



class OficioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado', 'modificado')
    list_display_links = ('id', 'nombre')
    search_fields = ('id', 'nombre')
    ordering = ('nombre', )
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('nombre',)
        }),
    )



class CentroTrabajoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado', 'modificado')
    list_display_links = ('id', 'nombre')
    search_fields = ('id', 'nombre')
    ordering = ('nombre', )
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('nombre',)
        }),
    )



admin.site.register(Oficio, OficioAdmin)
admin.site.register(CentroTrabajo, CentroTrabajoAdmin)
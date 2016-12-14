from django.contrib import admin
from item.models import TipoOficio, TipoCentroTrabajo



class TipoOficioAdmin(admin.ModelAdmin):
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



class TipoCentroTrabajoAdmin(admin.ModelAdmin):
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



admin.site.register(TipoOficio, TipoOficioAdmin)
admin.site.register(TipoCentroTrabajo, TipoCentroTrabajoAdmin)
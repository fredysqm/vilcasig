from django.contrib import admin
from social.models import Ingreso, CentroTrabajo, Oficio



class IngresoAdmin(admin.ModelAdmin):
    list_display = ('centro_poblado', 'nro_habitantes', 'nro_familias', 'creado', 'modificado')
    list_select_related = ('centro_poblado', )
    search_fields = ('centro_poblado__nombre',)
    ordering = ('centro_poblado__nombre', )
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('centro_poblado', 'nro_habitantes')
        }),
        ('Ingresos económicos mensuales', {
            'fields': ('m200','m201_499','m501_999','m1000'),
        }),
    )


class CentroTrabajoAdmin(admin.ModelAdmin):
    list_display = ('id', 'centro_poblado', 'tipo_centro_trabajo', 'porcentaje', 'creado', 'modificado')
    list_display_links = ('id', 'centro_poblado', )
    list_select_related = ('centro_poblado', 'tipo_centro_trabajo')
    list_filter = ('tipo_centro_trabajo',  'centro_poblado', )
    search_fields = ('centro_poblado__nombre', 'tipo_centro_trabajo__nombre')
    ordering = ('id', )
    list_per_page = 50



class OficioAdmin(admin.ModelAdmin):
    list_display = ('id', 'centro_poblado', 'tipo_oficio', 'porcentaje', 'creado', 'modificado')
    list_display_links = ('id', 'centro_poblado', )
    list_select_related = ('centro_poblado', 'tipo_oficio')
    list_filter = ('tipo_oficio',  'centro_poblado', )
    search_fields = ('centro_poblado__nombre', 'tipo_oficio__nombre')
    ordering = ('id', )
    list_per_page = 50



admin.site.register(Ingreso, IngresoAdmin)
admin.site.register(CentroTrabajo, CentroTrabajoAdmin)
admin.site.register(Oficio, OficioAdmin)
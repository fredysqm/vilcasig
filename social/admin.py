from django.contrib import admin
from social.models import Ingreso



class IngresoAdmin(admin.ModelAdmin):
    list_display = ('centro_poblado', 'nro_habitantes', 'nro_familias')
    list_select_related = ('centro_poblado', )
    search_fields = ('centro_poblado',)
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


admin.site.register(Ingreso, IngresoAdmin)
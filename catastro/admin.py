from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.forms.widgets import Textarea
from catastro.models import Sector, Manzana, Lote



class SectorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'centro_poblado', '_creado', '_modificado')
    list_select_related = ('centro_poblado', )
    search_fields = ('centro_poblado__nombre',)
    ordering = ('centro_poblado__nombre', )
    list_per_page = 50
    formfield_overrides = {
        models.PolygonField: {'widget': Textarea }
    }
    fieldsets = (
        (None, {
            'fields': ('centro_poblado', 'codigo', 'nombre', 'geom')
        }),
    )


class ManzanaAdmin(admin.ModelAdmin):
    list_display = ('id', 'sector__centro_poblado__nombre', 'sector__nombre', 'codigo', 'letra', '_creado', '_modificado')
    #list_editable = ('codigo', 'letra',)
    search_fields = ('sector__nombre',)
    ordering = ('codigo', )
    list_per_page = 50
    formfield_overrides = {
        models.PolygonField: {'widget': Textarea }
    }
    fieldsets = (
        (None, {
            'fields': ('sector', 'codigo', 'letra', 'geom')
        }),
    )

    def sector__nombre(self, obj):
        return obj.sector.nombre
    sector__nombre.short_description = 'sector'

    def sector__centro_poblado__nombre(self, obj):
        return obj.sector.centro_poblado.nombre
    sector__centro_poblado__nombre.short_description = 'centro poblado'

    def get_queryset(self, request):
        return super(ManzanaAdmin, self).get_queryset(request).select_related('sector__centro_poblado')


class LoteAdmin(admin.ModelAdmin):
    list_display = ('codigo',  'manzana', '_creado', '_modificado')
    search_fields = ('manzana__nombre',)
    ordering = ('codigo', )
    list_per_page = 50
    formfield_overrides = {
        models.PolygonField: {'widget': Textarea }
    }
    fieldsets = (
        (None, {
            'fields': ('manzana', 'codigo', 'geom')
        }),
    )


admin.site.register(Sector, SectorAdmin,)
admin.site.register(Manzana, ManzanaAdmin,)
admin.site.register(Lote, LoteAdmin,)

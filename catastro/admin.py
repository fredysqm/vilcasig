from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.forms.widgets import Textarea
from catastro.models import Sector, Manzana


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
    list_display = ('codigo', 'letra', 'sector', '_creado', '_modificado')
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

admin.site.register(Sector, SectorAdmin,)
admin.site.register(Manzana, ManzanaAdmin,)

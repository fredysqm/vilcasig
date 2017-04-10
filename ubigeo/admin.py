from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.forms.widgets import Textarea
from ubigeo.models import Departamento, Provincia, Distrito, CentroPoblado


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creado', 'modificado')
    list_display_links = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre',)
    ordering = ('codigo', )
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre',)
        }),
        ('Geometria', {
            'classes': ('collapse',),
            'fields': ('geom',),
        }),
    )


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'departamento', 'creado', 'modificado')
    list_display_links = ('codigo', 'nombre')
    list_select_related = ('departamento', )
    raw_id_fields = ('departamento',)
    search_fields = ('codigo', 'nombre', )
    list_filter = ('departamento', )
    ordering = ('codigo', )
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre', 'departamento')
        }),
        ('Geometria', {
            'classes': ('collapse',),
            'fields': ('geom',),
        }),
    )

class DistritoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'provincia', 'creado', 'modificado')
    list_display_links = ('codigo', 'nombre')
    list_select_related = ('provincia', )
    raw_id_fields = ('provincia',)
    search_fields = ('codigo', 'nombre',)
    ordering = ('codigo', )
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre', 'provincia')
        }),
        ('Geometria', {
            'classes': ('collapse',),
            'fields': ('geom',),
        }),
    )


class CentroPobladoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'distrito', 'creado', 'modificado')
    list_display_links = ('codigo', 'nombre')
    list_select_related = ('distrito', )
    raw_id_fields = ('distrito',)
    search_fields = ('codigo', 'nombre',)
    ordering = ('nombre', )
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre', 'distrito')
        }),
        ('Geometria', {
            'classes': ('collapse',),
            'fields': ('geom',),
        }),
    )
    formfield_overrides = {
        models.MultiPointField: {'widget': Textarea }
    }



admin.site.register(Departamento, DepartamentoAdmin,)
admin.site.register(Provincia, ProvinciaAdmin,)
admin.site.register(Distrito, DistritoAdmin,)
admin.site.register(CentroPoblado, CentroPobladoAdmin,)
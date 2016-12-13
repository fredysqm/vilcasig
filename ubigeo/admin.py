from django.contrib import admin
from ubigeo.models import Departamento, Provincia, Distrito, CentroPoblado, Perimetro


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
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
    list_display = ('codigo', 'nombre', 'departamento')
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
    list_display = ('codigo', 'nombre', 'provincia')
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
    list_display = ('codigo', 'nombre', 'distrito')
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


class PerimetroAdmin(admin.ModelAdmin):
    list_display = ('centro_poblado',)
    list_select_related = ('centro_poblado', )
    search_fields = ('centro_poblado',)
    ordering = ('centro_poblado__nombre', )
    list_per_page = 50


admin.site.register(Departamento, DepartamentoAdmin,)
admin.site.register(Provincia, ProvinciaAdmin,)
admin.site.register(Distrito, DistritoAdmin,)
admin.site.register(CentroPoblado, CentroPobladoAdmin,)
admin.site.register(Perimetro, PerimetroAdmin)
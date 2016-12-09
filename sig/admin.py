from django.contrib import admin
from sig.models import PredioMatriz, Departamento, Provincia, Distrito


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    search_fields = ('codigo', 'nombre',)
    ordering = ('codigo', )
    list_per_page = 25


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'departamento')
    list_select_related = ('departamento', )
    search_fields = ('codigo', 'nombre', )
    list_filter = ('departamento', )
    ordering = ('codigo', )
    list_per_page = 25


class DistritoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'provincia')
    search_fields = ('codigo', 'nombre',)
    ordering = ('codigo', )
    list_per_page = 25


#admin.site.register(PredioMatriz,)
admin.site.register(Departamento, DepartamentoAdmin,)
admin.site.register(Provincia, ProvinciaAdmin,)
admin.site.register(Distrito, DistritoAdmin,)
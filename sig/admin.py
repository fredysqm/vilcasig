from django.contrib import admin
#from sig.models import Departamento, Provincia, Distrito, CentroPoblado, Perimetro, Familia


# class DepartamentoAdmin(admin.ModelAdmin):
#     list_display = ('codigo', 'nombre',)
#     search_fields = ('codigo', 'nombre',)
#     ordering = ('codigo', )
#     list_per_page = 25


# class ProvinciaAdmin(admin.ModelAdmin):
#     list_display = ('codigo', 'nombre', 'departamento')
#     list_select_related = ('departamento', )
#     raw_id_fields = ('departamento',)
#     search_fields = ('codigo', 'nombre', )
#     list_filter = ('departamento', )
#     ordering = ('codigo', )
#     exclude = ('geom',)
#     list_per_page = 25


# class DistritoAdmin(admin.ModelAdmin):
#     list_display = ('codigo', 'nombre', 'provincia')
#     search_fields = ('codigo', 'nombre',)
#     raw_id_fields = ('provincia',)
#     ordering = ('codigo', )
#     exclude = ('geom',)
#     list_per_page = 25


# class FamiliaAdmin(admin.ModelAdmin):
#     list_display = ('codigo', 'nombre', 'provincia')
#     search_fields = ('codigo', 'nombre',)
#     raw_id_fields = ('provincia',)
#     ordering = ('codigo', )
#     exclude = ('geom',)
#     list_per_page = 25


# admin.site.register(Departamento, DepartamentoAdmin,)
# admin.site.register(Provincia, ProvinciaAdmin,)
# admin.site.register(Distrito, DistritoAdmin,)
# admin.site.register(CentroPoblado,)
# admin.site.register(Perimetro,)
# admin.site.register(Familia,)
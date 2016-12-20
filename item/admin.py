from django.contrib import admin
from item.models import TipoOficio, TipoProductoAgricola, TipoUnidadMedida, TipoProductoDestino



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
admin.site.register(TipoOficio, TipoOficioAdmin)



class TipoProductoAgricolaAdmin(admin.ModelAdmin):
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
admin.site.register(TipoProductoAgricola, TipoProductoAgricolaAdmin)



class TipoUnidadMedidaAdmin(admin.ModelAdmin):
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
admin.site.register(TipoUnidadMedida, TipoUnidadMedidaAdmin)



class TipoProductoDestinoAdmin(admin.ModelAdmin):
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
admin.site.register(TipoProductoDestino, TipoProductoDestinoAdmin)
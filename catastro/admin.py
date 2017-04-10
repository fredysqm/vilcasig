from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.forms.widgets import Textarea
from catastro.models import Perimetro



class PerimetroAdmin(admin.ModelAdmin):
    list_display = ('centro_poblado', 'creado', 'modificado')
    list_select_related = ('centro_poblado', )
    search_fields = ('centro_poblado__nombre',)
    ordering = ('centro_poblado__nombre', )
    list_per_page = 50
    formfield_overrides = {
        models.PolygonField: {'widget': Textarea }
    }

admin.site.register(Perimetro, PerimetroAdmin,)

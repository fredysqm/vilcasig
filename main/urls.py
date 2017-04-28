from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'', include('sig.urls')),
    url(r'^auth/', include('autenticacion.urls')),
    url(r'^admin/', admin.site.urls),
]

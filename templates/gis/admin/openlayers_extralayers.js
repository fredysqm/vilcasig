{% extends "gis/admin/openlayers.js" %}

{% block extra_layers %}
    {{ module }}.layers.limite = new OpenLayers.Layer.WMS( "Limites", "http://sig.mdv.net:9182/cgi-bin/sig/qgis_mapserv.fcgi", {layers: 'limite'} );
    {{ module }}.map.addLayer({{ module }}.layers.limite);

    {{ module }}.layers.vilcabamba = new OpenLayers.Layer.WMS( "Vilcabamba", "http://sig.mdv.net:9182/cgi-bin/sig/qgis_mapserv.fcgi", {layers: 'vilcabamba_mosaico'} );
    {{ module }}.map.addLayer({{ module }}.layers.vilcabamba);
{% endblock extra_layers %}
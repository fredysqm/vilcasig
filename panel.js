Ext.require([
    'GeoExt.component.Map',
    'GeoExt.data.store.LayersTree'
]);

var mapComponent;
var mapPanel;
var treePanel;

Ext.application({
    name: 'BasicTree',
    launch: function() {
        var source1;
        var source2;
        var source3;
        var source4;
        var source5;
        var source6;
        var source7;
        var source8;
        var source9;
        var source10;
        var layer1;
        var layer2;
        var layer3;
        var layer4;
        var layer5;
        var layer6;
        var layer7;
        var layer8;
        var layer9;
        var layer10;
        var layer11;
        var layer12;
        var olMap;
        var treeStore;
        var strWMSVilca;


        /*source1 = new ol.source.TileWMS({
            url: 'http://ows.terrestris.de/osm-gray/service',
            params: {'LAYERS': 'OSM-WMS', 'TILED': true}
        });
        layer1 = new ol.layer.Tile({
            source: source1,
            name: 'Base',
            description: 'Capa base',
            visible: true
        });*/


        /*source1 = new ol.source.OSM();
        layer1 = new ol.layer.Tile({
            source: source1
        });*/


        source1 = new ol.source.TileWMS({
            url: 'https://ows.terrestris.de/osm/service?"',
            params: {'LAYERS': 'OSM-WMS', 'TILED': true}
        });
        layer1 = new ol.layer.Tile({
            source: source1,
            name: 'Base',
            description: 'Capa base',
            visible: true
        });

        /*var map = new OpenLayers.Map({allOverlays: true, fallThrough: true});

        var wms = new OpenLayers.Layer.WMS(
            "OpenStreetMap WMS",
            "https://ows.terrestris.de/osm/service?",
            {layers: 'OSM-WMS'},
            {
                attribution: '&copy; terrestris GmbH & Co. KG <br>' +
                    'Data &copy; OpenStreetMap ' +
                    '<a href="http://www.openstreetmap.org/copyright/en"' +
                    'target="_blank">contributors<a>'
            }
        );*/

        strWMSVilca = 'http://sig.mdv.net:9182/cgi-bin/sig/qgis_mapserv.fcgi';

        source2 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'VILCABAMBA', 'TILED': true}
        });
        layer2 = new ol.layer.Tile({
            source: source2,
            name: 'Limite distrital',
            description: 'Limite distrital',
            visible: true
        });

        source3 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'RIOS', 'TILED': true}
        });
        layer3 = new ol.layer.Tile({
            source: source3,
            name: 'Hidrografia',
            description: 'Hidrografia',
            visible: true
        });

        source4 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'CCPP', 'TILED': true}
        });
        layer4 = new ol.layer.Tile({
            source: source4,
            name: 'Centros Poblados',
            description: 'Centros Poblados',
            visible: true
        });

        source5 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'CURVAS', 'TILED': true}
        });
        layer5 = new ol.layer.Tile({
            source: source5,
            name: 'Curvas de Nivel',
            description: 'Curvas de Nivel',
            visible: false
        });

        source6 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'Lt_Vilcabamba', 'TILED': true}
        });
        layer6 = new ol.layer.Tile({
            source: source6,
            name: 'LtVilcabamba',
            description: 'LtVilcabamba',
            visible: false
        });


        source7 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'DEPARTAMENTO', 'TILED': true}
        });
        layer7 = new ol.layer.Tile({
            source: source7,
            name: 'DEPARTAMENTO',
            description: 'DEPARTAMENTO',
            visible: true
        });

        source8 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'PROVINCIA', 'TILED': true}
        });
        layer8 = new ol.layer.Tile({
            source: source8,
            name: 'PROVINCIA',
            description: 'PROVINCIA',
            visible: true
        });

        source9 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'DISTRITO', 'TILED': true}
        });
        layer9 = new ol.layer.Tile({
            source: source9,
            name: 'DISTRITO',
            description: 'DISTRITO',
            visible: true
        });

        source10 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'PREDIOS_MATRICES', 'TILED': true}
        });
        layer10 = new ol.layer.Tile({
            source: source10,
            name: 'PREDIOS_MATRICES',
            description: 'PREDIOS_MATRICES',
            visible: true
        });


        layer11 = new ol.layer.Tile({
          visible: true,
          preload: Infinity,
          source: new ol.source.BingMaps({
            key: 'Ah50MLZcGai9LY5lUAqrOLAMWNDLdp4xjdkNLJYACHuQtqvQ7osDRytwJXnkJDH3',
            imagerySet: 'Aerial',
            // use maxZoom 19 to see stretched tiles instead of the BingMaps
            // "no photos at this zoom level" tiles
            maxZoom: 19
          })
        });


		var zoomslider;
		var scaleLineControl = new ol.control.ScaleLine();
		var view = new ol.View({
                center: [-8138700, -1475000],
                zoom: 10
            });
        olMap = new ol.Map({
            loadTilesWhileInteracting: true,
			controls: ol.control.defaults().extend([
			  new ol.control.FullScreen()
			]).extend([
				scaleLineControl
			]),
            layers: [layer11, layer5, layer2, layer3, layer4, layer6, layer7, layer8, layer9, layer10],
            view: view
        });
        zoomslider = new ol.control.ZoomSlider();
        olMap.addControl(zoomslider);

        mapComponent = Ext.create('GeoExt.component.Map', {
            map: olMap
        });

      olMap.on('singleclick', function(evt) {
        //document.getElementById('description').innerHTML = '';
        var viewResolution = /** @type {number} */ (view.getResolution());
        var url = source4.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, 'EPSG:3857',
            {'INFO_FORMAT': 'application/json'});
        if (url) {
          //document.getElementById('description').innerHTML = '<iframe seamless src="' + url + '"></iframe>';
          //alert(url);
          $.getJSON(url, function(data) {
                alert(data);
            });
        }
      });

      /*olMap.on('pointermove', function(evt) {
        if (evt.dragging) {
          return;
        }
        var pixel = olMap.getEventPixel(evt.originalEvent);
        var hit = olMap.forEachLayerAtPixel(pixel, function() {
          return true;
        });
        olMap.getTargetElement().style.cursor = hit ? 'pointer' : '';
      });*/

        mapPanel = Ext.create('Ext.panel.Panel', {
            region: 'center',
            border: false,
            layout: 'fit',
            items: [mapComponent]
        });

        treeStore = Ext.create('GeoExt.data.store.LayersTree', {
            layerGroup: olMap.getLayerGroup()
        });

        treePanel = Ext.create('Ext.tree.Panel', {
            title: 'SIG Vilcabamba',
            viewConfig: {
                plugins: {ptype: 'treeviewdragdrop'}
            },
            store: treeStore,
            rootVisible: false,
            flex: 1,
            border: false
        });

        var description = Ext.create('Ext.panel.Panel', {
            contentEl: 'description',
            title: 'Detalle',
            height: 200,
            border: false,
            bodyPadding: 5
        });

        Ext.create('Ext.Viewport', {
            layout: 'border',
            items: [
                mapPanel,
                {
                    xtype: 'panel',
                    region: 'west',
                    width: 250,
                    layout: {
                        type: 'vbox',
                        align: 'stretch'
                    },
                    items: [
                        treePanel,
                        description
                    ]
                }
            ]
        });
    }
});

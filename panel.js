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
        var layer1;
        var layer2;
        var layer3;
        var layer4;
        var layer5;
		var layer6;
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

        strWMSVilca = 'http://192.198.1.118:9181/geoserver/Vilcabamba/wms?';

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
            params: {'LAYERS': 'RIOS_VILCABAMBA', 'TILED': true}
        });
        layer3 = new ol.layer.Tile({
            source: source3,
            name: 'Hidrografia',
            description: 'Hidrografia',
            visible: true
        });

        source4 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'CCPP_VILCABAMBA', 'TILED': true}
        });
        layer4 = new ol.layer.Tile({
            source: source4,
            name: 'Centros Poblados',
            description: 'Centros Poblados',
            visible: true
        });

        source5 = new ol.source.TileWMS({
            url: strWMSVilca,
            params: {'LAYERS': 'CURVAS_VILCABAMBA', 'TILED': true}
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


		var zoomslider;
		var scaleLineControl = new ol.control.ScaleLine();
		var view = new ol.View({
                center: [-8138700, -1475000],
                zoom: 10
            });
        olMap = new ol.Map({
			controls: ol.control.defaults().extend([
			  new ol.control.FullScreen()
			]).extend([
				scaleLineControl
			]),
            layers: [layer1, layer5, layer2, layer3, layer4, layer6],
            view: view
        });
        zoomslider = new ol.control.ZoomSlider();
        olMap.addControl(zoomslider);

        mapComponent = Ext.create('GeoExt.component.Map', {
            map: olMap
        });

      olMap.on('singleclick', function(evt) {
        document.getElementById('description').innerHTML = '';
        var viewResolution = /** @type {number} */ (view.getResolution());
        var url = source4.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, 'EPSG:3857',
            {'INFO_FORMAT': 'application/json'});
        if (url) {
          document.getElementById('description').innerHTML =
              '<iframe seamless src="' + url + '"></iframe>';
        }
      });

      olMap.on('pointermove', function(evt) {
        if (evt.dragging) {
          return;
        }
        var pixel = olMap.getEventPixel(evt.originalEvent);
        var hit = olMap.forEachLayerAtPixel(pixel, function() {
          return true;
        });
        olMap.getTargetElement().style.cursor = hit ? 'pointer' : '';
      });

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

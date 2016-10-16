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
        var layer1;
        var layer2;
        var layer3;
        var layer4;
        var olMap;
        var treeStore;


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

        source2 = new ol.source.TileWMS({
            url: 'http://sig-vilcabamba.svr64.xyz:9181/geoserver/vilcabamba/wms?',
            params: {'LAYERS': 'VILCABAMBA', 'TILED': true}
        });
        layer2 = new ol.layer.Tile({
            source: source2,
            name: 'Limite distrital',
            description: 'Limite distrital',
            visible: true
        });

        source3 = new ol.source.TileWMS({
            url: 'http://sig-vilcabamba.svr64.xyz:9181/geoserver/vilcabamba/wms?',
            params: {'LAYERS': 'RIOS_VILCABAMBA', 'TILED': true}
        });
        layer3 = new ol.layer.Tile({
            source: source3,
            name: 'Hidrografia',
            description: 'Hidrografia',
            visible: true
        });

        source4 = new ol.source.TileWMS({
            url: 'http://sig-vilcabamba.svr64.xyz:9181/geoserver/vilcabamba/wms?',
            params: {'LAYERS': 'CCPP_VILCABAMBA', 'TILED': true}
        });
        layer4 = new ol.layer.Tile({
            source: source4,
            name: 'Centros Poblados',
            description: 'Centros Poblados',
            visible: true
        });

        olMap = new ol.Map({
            layers: [layer1, layer2, layer3, layer4],
            view: new ol.View({
                center: [-8138700, -1475000],
                zoom: 10
            })
        });

        mapComponent = Ext.create('GeoExt.component.Map', {
            map: olMap
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

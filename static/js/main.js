Ext.Loader.setConfig({
    enabled: true,
    paths: {
        'GeoExt': '/static/lib/geoext/src'
    }
});

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
        var olMap;
        var treeStore;

        var strWMSVilca = 'http://sig.mdv.net:9182/cgi-bin/sig/qgis_mapserv.fcgi';

        var sig_layers = [

            new ol.layer.Tile({
                visible: true,
                preload: Infinity,
                name: 'Base',
                description: 'Base_',
                source: new ol.source.BingMaps({
                    key: 'Ah50MLZcGai9LY5lUAqrOLAMWNDLdp4xjdkNLJYACHuQtqvQ7osDRytwJXnkJDH3',
                    imagerySet: 'Aerial',
                    maxZoom: 30
                }),
            }),

            new ol.layer.Tile({
                name: 'Distrito',
                description: 'Distrito_',
                visible: true,
                source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'DISTRITO', 'TILED': true }
                }),
            }),

            new ol.layer.Tile({
                name: 'Provincia',
                description: 'Provincia_',
                visible: true,
                    source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'PROVINCIA', 'TILED': true }
                }),
            }),

            new ol.layer.Tile({
                name: 'Departamento',
                description: 'Departamento_',
                visible: true,
                source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'DEPARTAMENTO', 'TILED': true }
                }),
            }),

            new ol.layer.Tile({
                name: 'Curvas de Nivel',
                description: 'Curvas de Nivel_',
                visible: false,
                source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'CURVAS_NIVEL', 'TILED': true }
                }),
            }),

            new ol.layer.Tile({
                name: 'Rios',
                description: 'Rios_',
                visible: true,
                source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'RIOS', 'TILED': true }
                }),
            }),

            new ol.layer.Tile({
                name: 'Rios Principales',
                description: 'Rios Principales_',
                visible: true,
                source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'RIOS_POLI', 'TILED': true }
                }),
            }),

            new ol.layer.Tile({
                name: 'Centros Poblados',
                description: 'Centros Poblados_',
                visible: true,
                source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'CCPP', 'TILED': true }
                }),
            }),

            new ol.layer.Tile({
                name: 'Predios Matrices',
                description: 'Predios Matrices_',
                visible: true,
                source: new ol.source.TileWMS({
                    url: strWMSVilca,
                    params: { 'LAYERS': 'PREDIOS_MATRICES', 'TILED': true }
                }),
            }),

        ];

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
            layers: sig_layers,
            view: view
        });
        zoomslider = new ol.control.ZoomSlider();
        olMap.addControl(zoomslider);

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

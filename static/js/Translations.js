/*
 *
 * Translations.js -- part of QGIS Web Client
 *
 * Copyright (2010-2012), The QGIS Project All rights reserved.
 * QGIS Web Client is released under a BSD license. Please see
 * https://github.com/qgis/qgis-web-client/blob/master/README
 * for the full text of the license and the list of contributors.
 *
*/

//indicating which of the help files have been translated already
var availableHelpLanguages = Array("en","es");

//list of available languages
var availableLanguages = new Array();
availableLanguages["en"] = {names:[], translator:"Andreas Neumann"}; //a (dot) neumann (at) carto (dot) net
availableLanguages["es"] = {names:[], translator:"Samuel Mesa, Diana Galindo, Germán Carrillo"}; // samuelmesa (at) gmail (dot) com , drgalindog (at) linuxmail (dot) org

//translations of languages
// first language index is fixed, second variable
// The string is the name of the first language translated in the second language.

//English;
availableLanguages["en"].names["en"] = "English";
availableLanguages["en"].names["es"] = "Inglés";

//Spanish
availableLanguages["es"].names["en"] = "Spanish";
availableLanguages["es"].names["es"] = "Español";

/***********************
Status messages
***********************/

//map loading string displayed when starting the map application
var mapAppLoadingString = new Array();
mapAppLoadingString["en"] = "Loading map application...";
mapAppLoadingString["es"] = "Cargando la aplicación del mapa...";

//indicating that map app was loaded and we are now loading the map
var mapLoadingString = new Array();
mapLoadingString["en"] = "Loading Map...";
mapLoadingString["es"] = "Cargando mapa...";

//mode string for navigation
var modeNavigationString = new Array();
modeNavigationString["en"] = "Mode: navigation. Shift/rectangle or mouse wheel for zooming.";
modeNavigationString["es"] = "Modo: navegación. Shift/rectángulo o rueda del ratón que desea zoom.";

//mode string for rectangle zoom
var modeZoomRectangle = new Array();
modeZoomRectangle["en"] = "Mode: zoom with rectangle. Draw rectangle over region you wish to zoom in.";
modeZoomRectangle["es"] = "Modo: zoom con rectángulo. Dibujar el rectángulo sobre la región que desea acercar.";

//mode string for attribute data detailed
var modeObjectIdentificationString = new Array();
modeObjectIdentificationString["en"] = "Mode: object identification. Move the mouse over an object to identify it, click it to view its attribute data.";
modeObjectIdentificationString["es"] = "Modo: Identificación de objeto. Mueva el cursor sobre un objeto para identificarlo, haga click sobre él para ver sus atributos.";

//mode string for map tips (display main attribute with tooltips)
var modeMapTipsString = new Array();
modeMapTipsString["en"] = "Mode: MapTips. Display on mouse over with Tooltips.";
modeMapTipsString["es"] = "Modo: MapTips. Despliega textos emergentes con el cursor del ratón.";

//mode measure distance
var modeMeasureDistanceString = new Array();
modeMeasureDistanceString["en"] = "Mode: measure distance. Finish with double click.";
modeMeasureDistanceString["es"] = "Modo: medir distancia. Finalizar con doble click.";

//mode measure area
var modeMeasureAreaString = new Array();
modeMeasureAreaString["en"] = "Mode: measure area. Finish with double click.";
modeMeasureAreaString["es"] = "Modo: medir área. Finalizar con doble click.";

//mode printing
var modePrintingString = new Array();
modePrintingString["en"] = "Mode: printing. Move or rotate the map extent. Print with the 'Print'-Button.";
modePrintingString["es"] = "Modo: imprimir. Mueva o rote la extensión del mapa. Imprima con el botón 'imprimir'.";

//indicating is waiting for print
var printLoadingString = new Array();
printLoadingString["en"] = "Printing initialised. Please wait...";
printLoadingString["es"] = "Impresión inicializada. Por favor espere...";
/***********************
GUI stuff
***********************/

//title of panel on the left
var leftPanelTitleString = new Array();
leftPanelTitleString["en"] = "Info and Tools";
leftPanelTitleString["es"] = "Información y herramientas";

//title of search panel
var searchPanelTitleString = new Array();
searchPanelTitleString["en"] = "Search";
searchPanelTitleString["es"] = "Buscar";

//text of theme Switcher button
var mapThemeButtonTitleString = new Array();
mapThemeButtonTitleString["en"] = "Map themes";
mapThemeButtonTitleString["es"] = "Temas de mapas";

//theme switcher window title
var themeSwitcherWindowTitleString = new Array();
themeSwitcherWindowTitleString["en"] = "Map theme choice";
themeSwitcherWindowTitleString["es"] = "Elección de tema de mapa";

//theme switcher filter label string
var themeSwitcherFilterLabelString = new Array();
themeSwitcherFilterLabelString["en"] = "Filter by map title: ";
themeSwitcherFilterLabelString["es"] = "Filtrar por título de mapa: ";

//theme switcher all themes string in list view
var themeSwitcherAllThemesListViewString = new Array();
themeSwitcherAllThemesListViewString["en"] = "All map themes";
themeSwitcherAllThemesListViewString["es"] = "Todos los temas de mapas";

var themeSwitcherTooltipResponsibleString = new Array();
themeSwitcherTooltipResponsibleString["en"] = "Responsible: ";
themeSwitcherTooltipResponsibleString["es"] = "Responsable: ";

//either tags or keywords
var themeSwitcherTooltipTagString = new Array();
themeSwitcherTooltipTagString["en"] = "Tags: ";
themeSwitcherTooltipTagString["es"] = "Etiquetas: ";

var themeSwitcherTooltipMapThemeString = new Array();
themeSwitcherTooltipMapThemeString["en"] = "Map theme: ";
themeSwitcherTooltipMapThemeString["es"] = "Tema de mapa: ";

var themeSwitcherTooltipUpdateString = new Array();
themeSwitcherTooltipUpdateString["en"] = "Update interval: ";
themeSwitcherTooltipUpdateString["es"] = "Intervalo de actualización: ";

var themeSwitcherTooltipLastUpdateString = new Array();
themeSwitcherTooltipLastUpdateString["en"] = "Last update: ";
themeSwitcherTooltipLastUpdateString["es"] = "Última actualización: ";

var themeSwitcherTooltipPwProtectedString = new Array();
themeSwitcherTooltipPwProtectedString["en"] = "password protected";
themeSwitcherTooltipPwProtectedString["es"] = "protegido por contraseña";

var emptyThemeSearchFieldString = new Array();
emptyThemeSearchFieldString["en"] = "Insert filter string";
emptyThemeSearchFieldString["es"] = "Inserte el texto para filtrar";

var resetThemeSearchFieldTooltipString = new Array();
resetThemeSearchFieldTooltipString["en"] = "Reset map theme search filter";
resetThemeSearchFieldTooltipString["es"] = "Borrar el filtro de búsqueda de temas de mapa";

//title of map panel
var mapPanelTitleString = new Array();
mapPanelTitleString["en"] = "Map";
mapPanelTitleString["es"] = "Mapa";

//title of map layer tree
var layerTreeTitleString = new Array();
layerTreeTitleString["en"] = "Map Layers";
layerTreeTitleString["es"] = "Capas";

//title of background layers
var backgroundLayerTitleString = new Array();
backgroundLayerTitleString["en"] = "Background Layers";
backgroundLayerTitleString["es"] = "Background Layers";

//title of layer order panel
var layerOrderPanelTitleString = new Array();
layerOrderPanelTitleString["en"] = "Layer order";
layerOrderPanelTitleString["es"] = "Orden de capa";

//tooltip of layer settings button in layer order panel
var layerOrderPanelLayerSettingsTooltipString = new Array();
layerOrderPanelLayerSettingsTooltipString["en"] = "Settings";
layerOrderPanelLayerSettingsTooltipString["es"] = "Ajustes";

//tooltip of remove layer button in layer order panel
var layerOrderPanelVisibilityChangeTooltipString = new Array();
layerOrderPanelVisibilityChangeTooltipString["en"] = "Change Layer Visibility";
layerOrderPanelVisibilityChangeTooltipString["es"] = "Cambiar la visibilidad de la capa";

//text when dragging layer in layer order panel
var layerOrderPanelMoveLayerTextString = new Array();
layerOrderPanelMoveLayerTextString["en"] = "Move layer";
layerOrderPanelMoveLayerTextString["es"] = "Mover capa";

//tooltip of transparency sliders in layer order panel
var layerOrderPanelTransparencyTooltipString = new Array();
layerOrderPanelTransparencyTooltipString["en"] = "Transparency {0}%";
layerOrderPanelTransparencyTooltipString["es"] = "Transparencia {0}%";

//title of legend tab
var legendTabTitleString = new Array();
legendTabTitleString["en"] = "Legend";
legendTabTitleString["es"] = "Leyenda";

//legend loading message in legend tab
var legendTabLoadingString = new Array();
legendTabLoadingString["en"] = "Loading legend, please wait...";
legendTabLoadingString["es"] = "Cargando leyenda, por favor espere...";

//title of metadata tab
var metadataTabTitleString = new Array();
metadataTabTitleString["en"] = "Metadata";
metadataTabTitleString["es"] = "Metadatos";

//title of help window
var helpWindowTitleString = new Array();
helpWindowTitleString["en"] = "Help";
helpWindowTitleString["es"] = "Ayuda";

//title of legend and per layer metadata window
var legendMetadataWindowTitleString = new Array();
legendMetadataWindowTitleString["en"] = "Legend and metadata information of layer";
legendMetadataWindowTitleString["es"] = "Información sobre la leyenda y los metadatos de la capa";

//title of metadata section
var metadataSectionTitleString = new Array();
metadataSectionTitleString["en"] = "Metadata of layer";
metadataSectionTitleString["es"] = "Metadatos de la capa";

//Abstract
var abstractString = new Array();
abstractString["en"] = "Abstract:";
abstractString["es"] = "Resumen:";

//title of legend and per layer metadata window
var layerQueryable = new Array();
layerQueryable["en"] = "This layer is queryable: ";
layerQueryable["es"] = "Esta capa se puede consultar: "; 

//in case we need a yes
var yesString = new Array();
yesString["en"] = "yes";
yesString["es"] = "si";

//in case we need a no
var noString = new Array();
noString["en"] = "no";
noString["es"] = "no";

//metadata: layer group
var layerGroupString = new Array();
layerGroupString["en"] = "Layer group";
layerGroupString["es"] = "Grupo de capas";

//metadata: display field (for tooltips)
var displayFieldString = new Array();
displayFieldString["en"] = "Display-Field";
displayFieldString["es"] = "Campo mostrado";

//metadata: coordinate systems
var coordinateSystemsString = new Array();
coordinateSystemsString["en"] = "Available Coordinate Systems";
coordinateSystemsString["es"] = "Sistemas de coordenadas disponibles";

//metadata: geographic extent
var geographicExtentString = new Array();
geographicExtentString["en"] = "Geographic Extent";
geographicExtentString["es"] = "Extensión geográfica";

//metadata: geographic extent
var westString = new Array();
westString["en"] = "west";
westString["es"] = "oeste";

//metadata: geographic extent
var eastString = new Array();
eastString["en"] = "east";
eastString["es"] = "este";

//metadata: geographic extent
var northString = new Array();
northString["en"] = "north";
northString["es"] = "norte";

//metadata: geographic extent
var southString = new Array();
southString["en"] = "south";
southString["es"] = "sur";

//attributes / fields
var attributesString = new Array();
attributesString["en"] = "Attributes / Fields";
attributesString["es"] = "Atributos";

//attribute name string
var attributeNameString = new Array();
attributeNameString["en"] = "Attribute name";
attributeNameString["es"] = "Nombre del atributo";

//attribute type string
var attributeTypeString = new Array();
attributeTypeString["en"] = "Type";
attributeTypeString["es"] = "Tipo";

//attribute comment string
var attributeCommentString = new Array();
attributeCommentString["en"] = "Comment";
attributeCommentString["es"] = "Comentario";

//attribute length string
var attributeLengthString = new Array();
attributeLengthString["en"] = "Length";
attributeLengthString["es"] = "Longitud";

//attribute length string
var attributePrecisionString = new Array();
attributePrecisionString["en"] = "Precision";
attributePrecisionString["es"] = "Precisión";

//label in main toolbar for object identification
var objectIdentificationTextLabel = new Array();
objectIdentificationTextLabel["en"] = "Object identification: ";
objectIdentificationTextLabel["es"] = "Identificación de objetos: ";

//Coordinate text label (coordinate display in bottom toolbar of main map window)
var coordinateTextLabel = new Array();
coordinateTextLabel["en"] = "Coordinate:";
coordinateTextLabel["es"] = "Coordenadas:";

//search
var searchFieldDefaultTextString = new Array();
searchFieldDefaultTextString["en"] = "Search (addresses, parcel-nrs, names, etc.)";
searchFieldDefaultTextString["es"] = "Buscar (direcciones, registros, nombres, etc.)";

//search button
var searchButtonString = new Array();
searchButtonString["en"] = "Search";
searchButtonString["es"] = "Buscar";

//reset button
var resetButtonString = new Array();
resetButtonString["en"] = "Clear";
resetButtonString["es"] = "Limpiar";

//please wait
var pleaseWaitString = new Array();
pleaseWaitString["en"] = "Please wait";
pleaseWaitString["es"] = "Por favor espere";

//search result
var searchResultString = new Array();
searchResultString["en"] = "Search result";
searchResultString["es"] = "Resultado de la búsqueda";

//network error
var networkErrorString = new Array();
networkErrorString["en"] = "Network error";
networkErrorString["es"] = "Error de red";

// missing or invalid search params
var missingOrInvalidSearchParams = new Array();
missingOrInvalidSearchParams["en"] = "Missing or invalid values in search form";
missingOrInvalidSearchParams["es"] = "Valores inválidos o faltantes en el formulario de búsqueda";

//search error
var searchErrorString = new Array();
searchErrorString["en"] = "Error during search";
searchErrorString["es"] = "Error en la búsqueda";

//search no records found
var searchNoRecordsFoundString = new Array();
searchNoRecordsFoundString["en"] = "No records found"; 
searchNoRecordsFoundString["es"] = "Error en la búsqueda";

//print settings toolbar title
var printSettingsToolbarTitleString = new Array();
printSettingsToolbarTitleString["en"] = "Print Settings";
printSettingsToolbarTitleString["es"] = "Configuración de impresión";

//print rotation text label
var printSettingsRotationTextlabelString = new Array();
printSettingsRotationTextlabelString["en"] = "Rotation: ";
printSettingsRotationTextlabelString["es"] = "Rotación: ";

//print button text
var printButtonTextString = new Array();
printButtonTextString["en"] = "Print";
printButtonTextString["es"] = "Imprimir";

//print cancel button text
var printCancelButtonTextString = new Array();
printCancelButtonTextString["en"] = "Cancel";
printCancelButtonTextString["es"] = "Cancelar";

//export toolbar title string
var exportSettingsToolbarTitleString = new Array();
exportSettingsToolbarTitleString["en"] = "Export Settings - Enter width/height or create rectangle in map.";
exportSettingsToolbarTitleString["es"] = "Configuración de exportación - Introduzca el ancho / altura o cree un rectángulo en el mapa.";

//export window title
var exportWindowTitleString = new Array();
exportWindowTitleString["en"] = "File is being generated by server.";
exportWindowTitleString["es"] = "El archivo está siendo generado por el servidor.";


//export width input field
var exportWidthInputField = new Array();
exportWidthInputField["en"] = "Width:";
exportWidthInputField["es"] = "Ancho";

//export height input field
var exportHeightInputField = new Array();
exportHeightInputField["en"] = "Height:";
exportHeightInputField["es"] = "Alto";

//text label lock export width/height ratio
var exportLockAspectRatioText = new Array();
exportLockAspectRatioText["en"] = "Lock Aspect Ratio";
exportLockAspectRatioText["es"] = "Bloquear proporción de aspecto";

//text label transparent
var exportTransparentOptionText = new Array();
exportTransparentOptionText["en"] = "Transparent";
exportTransparentOptionText["es"] = "Transparente";

//export button text string
var exportButtonTextString = new Array();
exportButtonTextString["en"] = "Export";
exportButtonTextString["es"] = "Exportar";

//export raster file properties text (window title)
var exportFilePropertyTextString = new Array();
exportFilePropertyTextString["en"] = "Rasterfile properties: ";
exportFilePropertyTextString["es"] = "Propiedades del raster: "; 

//export raster file copy/save hint (window title)
var exportSaveCopyHintText = new Array();
exportSaveCopyHintText["en"] = "Use context menu (right click) to save or copy file.";
exportSaveCopyHintText["es"] = "Utilice el menú contextual (clic derecho) para guardar o copiar el archivo.";

//DXF export disclaimer window title
var DXFExportDisclaimerWindowTitle = new Array();
DXFExportDisclaimerWindowTitle["en"] = "Disclaimer regarding DXF data download and usage.";
DXFExportDisclaimerWindowTitle["es"] = "Exención de responsabilidad con respecto a la descarga y uso de datos de DXF.";

//DXF export disclaimer accept button
var acceptDXFDisclaimerButtonText = new Array();
acceptDXFDisclaimerButtonText["en"] = "Accept";
acceptDXFDisclaimerButtonText["es"] = "Aceptar";

//DXF export disclaimer decline button
var declineDXFDisclaimerButtonText = new Array();
declineDXFDisclaimerButtonText["en"] = "Decline";
declineDXFDisclaimerButtonText["es"] = "Declinar";

//DXF export window title
var DXFExportWindowTitleString = new Array();
DXFExportWindowTitleString["en"] = "DXF Export of the current map extent - Please select a symbology map scale";
DXFExportWindowTitleString["es"] = "DXF Exportación de la extensión del mapa actual - Seleccione una escala de mapa de simbología";

//DXF export symbology scale label
var DXFExportSymbologyScaleLabel = new Array();
DXFExportSymbologyScaleLabel["en"] = "Symbology Scale: ";
DXFExportSymbologyScaleLabel["es"] = "Escala de simbología: ";

//area limit for the DXF export label
var DXFExportAreaLimitLabel = new Array();
DXFExportAreaLimitLabel["en"] = "Area limit for export: ";
DXFExportAreaLimitLabel["es"] = "Límite de área para exportación: ";

//area limit for the DXF export label
var DXFExportCurrentAreaLabel = new Array();
DXFExportCurrentAreaLabel["en"] = "Current area: ";
DXFExportCurrentAreaLabel["es"] = "Área actual: ";

//no limit for the DXF export label
var DXFExportNoAreaLimitLabel = new Array();
DXFExportNoAreaLimitLabel["en"] = "no limit";
DXFExportNoAreaLimitLabel["es"] = "sin límite"; 

//objectIdentificationModeStrings
var objectIdentificationModeString = new Array();
objectIdentificationModeString["topMostHit"] = new Array();
objectIdentificationModeString["topMostHit"]["en"] = "Topmost hit";
objectIdentificationModeString["topMostHit"]["es"] = "Capa superior";

objectIdentificationModeString["allLayers"] = new Array();
objectIdentificationModeString["allLayers"]["en"] = "All layers";
objectIdentificationModeString["allLayers"]["es"] = "Todas las capas";

objectIdentificationModeString["activeLayers"] = new Array();
objectIdentificationModeString["activeLayers"]["en"] = "Active Layer";
objectIdentificationModeString["activeLayers"]["es"] = "Capa activa";

//measure distance result prefix
var measureDistanceResultPrefixString = new Array();
measureDistanceResultPrefixString["en"] = "Distance";
measureDistanceResultPrefixString["es"] = "Distancia";

//distance prefix for result:
var measureAreaResultPrefixString = new Array();
measureAreaResultPrefixString["en"] = "Area";
measureAreaResultPrefixString["es"] = "Área";

/***********************
Tooltips
***********************/

//zoom rectangle tooltip
var zoomRectangleTooltipString = new Array();
zoomRectangleTooltipString["en"] = "Zoom with rectangle";
zoomRectangleTooltipString["es"] = "Zoom con rectángulo";

//zoom to full view
var zoomFullViewTooltipString = new Array();
zoomFullViewTooltipString["en"] = "Zoom to the maximum map extent";
zoomFullViewTooltipString["es"] = "Zoom a la extensión máxima ";

//navigation history backward
var navigationHistoryBackwardTooltipString = new Array();
navigationHistoryBackwardTooltipString["en"] = "Navigation history backward";
navigationHistoryBackwardTooltipString["es"] = "Ir a la vista anterior";

//navigation history forward
var navigationHistoryForwardTooltipString = new Array();
navigationHistoryForwardTooltipString["en"] = "Navigation history forward";
navigationHistoryForwardTooltipString["es"] = "Ir a la vista posterior";

//discrete zoom in button above zoom slider
var zoomInTooltipString = new Array();
zoomInTooltipString["en"] = "Zoom in (discrete step)";
zoomInTooltipString["es"] = "Acercar (un nivel)";

//discrete zoom in button above zoom slider
var zoomOutTooltipString = new Array();
zoomOutTooltipString["en"] = "Zoom out (discrete step)";
zoomOutTooltipString["es"] = "Alejar (un nivel)";

//object identification tooltip
var objIdentificationTooltipString = new Array();
objIdentificationTooltipString["en"] = "Object identification (attribute data)";
objIdentificationTooltipString["es"] = "Indentificación de objetos (atributos)";

//MapTips tooltip
var mapTipsTooltipString = new Array();
mapTipsTooltipString["en"] = "Display MapTips (attribute data)";
mapTipsTooltipString["es"] = "Desplegar textos emergentes (atributos)";

//Measure Distance
var measureDistanceTooltipString = new Array();
measureDistanceTooltipString["en"] = "Measure distance";
measureDistanceTooltipString["es"] = "Medir distancia";

//Measure Area
var measureAreaTooltipString = new Array();
measureAreaTooltipString["en"] = "Measure area";
measureAreaTooltipString["es"] = "Medir área";

//Print Map
var printMapTooltipString = new Array();
printMapTooltipString["en"] = "Print Map";
printMapTooltipString["es"] = "Imprimir mapa";

//Print Map disabled
var printMapDisabledTooltipString = new Array();
printMapDisabledTooltipString["en"] = "Print disabled, no layout is defined in the QGIS project";
printMapDisabledTooltipString["es"] = "Imprimir deshabilitado, no hay formato definido en el proyecto de QGIS";

//Export Map
var exportMapTooltipString = new Array();
exportMapTooltipString["en"] = "Export Map as Raster";
exportMapTooltipString["es"] = "Exportar mapa como ráster";

//Export DXF
var exportDXFTooltipString = new Array();
exportDXFTooltipString["en"] = "Export map extent as DXF";
exportDXFTooltipString["es"] = "Exportar extensión de mapa como DXF";

//Send permalink
var sendPermalinkTooltipString = new Array();
sendPermalinkTooltipString["en"] = "Email a link to this map";
sendPermalinkTooltipString["es"] = "Enviar un enlace a este mapa por correo electrónico";

//Send permalink
var sendPermalinkLinkFromString = new Array();
sendPermalinkLinkFromString["en"] = "Link from ";
sendPermalinkLinkFromString["es"] = "Enlace desde ";

//Show Help
var showHelpTooltipString = new Array();
showHelpTooltipString["en"] = "Show Help";
showHelpTooltipString["es"] = "Mostrar ayuda";

//Geonames loading string
var geonamesLoadingString = new Array();
geonamesLoadingString["en"] = "Search in Geonames...";
geonamesLoadingString["es"] = "Buscar en Geonames...";

//Geonames empty string
var geonamesEmptyString = new Array();
geonamesEmptyString["en"] = "Search location in Geonames";
geonamesEmptyString["es"] = "Buscar lugar en Geonames";

//Reset Search Field
var resetSearchFieldTooltipString = new Array();
resetSearchFieldTooltipString["en"] = "Reset/empty Searchfield";
resetSearchFieldTooltipString["es"] = "Limpiar campo de búsqueda";

//print window title
var printWindowTitleString = new Array();
printWindowTitleString["en"] = "The server is generating a PDF file. For correct up to scale printing please deactivate the option 'Fit to Page'!";
printWindowTitleString["es"] = "El servidor está generando un archivo PDF. Para corregir la escala de impresión desactive la opción 'Ajustar a la página'!";

//print object data alternative string in case no pdf plugin is present in browser
//attention: single quotes around string, partially html formatting
var printingObjectDataAlternativeString1 = new Array();
printingObjectDataAlternativeString1["en"] = 'It looks like your browser cannot open PDF files directly. Not a big problem - you can <a href="';
printingObjectDataAlternativeString1["es"] = 'Su navegador no puede abrir archivos PDF directamente. No es problema - usted puede <a href="';

//the second part of the string after the URL
//attention: single quotes around string, partially html formatting
var printingObjectDataAlternativeString2 = new Array();
printingObjectDataAlternativeString2["en"] = '">download the PDF file here.</a>.</p></object>';
printingObjectDataAlternativeString2["es"] = '">descargar el archivo PDF aquí.</a>.</p></object>';

//print button tooltip
var printButtonTooltipString = new Array();
printButtonTooltipString["en"] = "Print (Generate PDF)";
printButtonTooltipString["es"] = "Imprimir (Generar PDF)";

//print cancel button tooltip
var printCancelButtonTooltipString = new Array();
printCancelButtonTooltipString["en"] = "Cancel Print (Close)";
printCancelButtonTooltipString["es"] = "Cancelar impresión (Cerrar)";

//export button tooltip
var exportButtonTooltipString = new Array();
exportButtonTooltipString["en"] = "Export to chosen file format";
exportButtonTooltipString["es"] = "Exportar al formato de archivo elegido";

//export cancel button tooltip
var exportCancelButtonTooltipString = new Array();
exportCancelButtonTooltipString["en"] = "Cancel Export";
exportCancelButtonTooltipString["es"] = "Cancelar exportación";

//theme switcher button tooltip
var mapThemeButtonTooltipString = new Array();
mapThemeButtonTooltipString["en"] = "Click to choose a new map theme";
mapThemeButtonTooltipString["es"] = "Haga click para escoger un nuevo tema de mapa";

//comment, if layer is outside scale range
var tooltipLayerTreeLayerOutsideScale = new Array();
tooltipLayerTreeLayerOutsideScale["en"] = "Visible at scales";
tooltipLayerTreeLayerOutsideScale["es"] = "Visible en las escalas";

/***********************
Error Messages
***********************/

//error messages on startup
var errMessageStartupMapParamString = new Array();
errMessageStartupMapParamString["en"] = "Startup-Parameter 'map' missing!";
errMessageStartupMapParamString["es"] = "Falta el parámetro de inicio 'map'!";

//additional startup error message
var errMessageStartupNotAllParamsFoundString = new Array();
errMessageStartupNotAllParamsFoundString["en"] = "Some mandatory startup paramaters are missing or an optional startup parameter is invalid.";
errMessageStartupNotAllParamsFoundString["es"] = "Faltan algunos parámetros obligatorios";

//error message if optional startExtent parameter is wrong
var errMessageExtentParamWrongPart1 = new Array();
errMessageExtentParamWrongPart1["en"] = "Start-parameter '";
errMessageExtentParamWrongPart1["es"] = "Parámetro de inicialización '";

//error message if optional startExtent parameter is wrong
var errMessageExtentParamWrongPart2 = new Array();
errMessageExtentParamWrongPart2["en"] = "' needs to be in OpenLayers.Bounds format: 'left,bottom,right,top'.";
errMessageExtentParamWrongPart2["es"] = "' debe estar en formato OpenLayers.Bounds: 'left,bottom,right,top'.";

//error message invalid language code, part 1
var errMessageInvalidLanguageCodeString1 = new Array();
errMessageInvalidLanguageCodeString1["en"] = "Invalid language code provided: ";
errMessageInvalidLanguageCodeString1["es"] = "El código de idioma es inválido: ";

//error message invalid language code, part 2
var errMessageInvalidLanguageCodeString2 = new Array();
errMessageInvalidLanguageCodeString2["en"] = "Switching back to default language ";
errMessageInvalidLanguageCodeString2["es"] = "Restableciendo el idioma por defecto ";

//error message of search combo network request title
var errMessageSearchComboNetworkRequestFailureTitleString = new Array();
errMessageSearchComboNetworkRequestFailureTitleString["en"] = "Network request failed";
errMessageSearchComboNetworkRequestFailureTitleString["es"] = "Falló la solicitud de red";

//error message of search combo network request detailed message - do not forget the \n at the end of the string!
var errMessageSearchComboNetworkRequestFailureString = new Array();
errMessageSearchComboNetworkRequestFailureString["en"] = "The network request for the geometry of the search result failed:\n";
errMessageSearchComboNetworkRequestFailureString["es"] = "Falló la solicitud de red para la geometría del resultado de la búsqueda:\n";

//error message when help is unavailable for selected language
var errMessageHelpFile = new Array();
errMessageHelpFile["en"] = "Help file unavailable for this language!\n";
errMessageHelpFile["es"] = "¡El archivo de ayuda no está disponible para este idioma!\n";

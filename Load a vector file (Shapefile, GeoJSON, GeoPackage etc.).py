# Load a vector file (Shapefile, GeoJSON, GeoPackage etc.)
layer_path = r"C:\Users\user\Downloads\your_vector_layer.shp"   # or .geojson, .gpkg
layer_name = "Layer_Name"

layer = QgsVectorLayer(layer_path,layer_name, "ogr")

if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
else:
    print("Layer failed to load")

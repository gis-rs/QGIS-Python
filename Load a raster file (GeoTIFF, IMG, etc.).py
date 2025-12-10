# Load a raster file (GeoTIFF, IMG, etc.)
raster_path = r"C:\Users\user\Downloads\your_image.tif"
layer_name = "Satellite Image"

raster = QgsRasterLayer(raster_path, layer_name)

if raster.isValid():
    QgsProject.instance().addMapLayer(raster)
else:
    print("Raster failed to load")

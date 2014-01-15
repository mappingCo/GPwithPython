from osgeo import ogr
from qgis.core import *
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PyQt4.QtCore import QFileInfo

#cargamos archivo puntos.shp
ruta_shp="C:\datos\puntos.shp"
informacion_shp = QFileInfo(ruta_shp)
nombre=informacion_shp.baseName()
try:
    capaPuntos=QgsVectorLayer(ruta_shp, nombre, "ogr")
    QgsMapLayerRegistry.instance().addMapLayer(capaPuntos)
    print "capa '"+ nombre+ "' cargada correctamente"
except:
     print "ha ocurrido un error, la capa no se pudo cargar"
#cargamos raster: EGM08_REDNAP.tif
ruta_raster="C:\datos\EGM08_REDNAP.tif"
informacion_raster = QFileInfo(ruta_raster)
nombreRaster= informacion_raster.baseName()
try:
    capaRaster=QgsRasterLayer(ruta_raster, nombreRaster)
    QgsMapLayerRegistry.instance().addMapLayer(capaRaster)
    print "capa '"+ nombreRaster+ "' cargada correctamente"
except:
    print "ha ocurrido un error, la capa no se pudo cargar"






    
from os import system,chdir
from osgeo import ogr
from osgeo import gdal
from sys import exit

#funcion que abre un archivo en carpeta datos (libreria ogr)
def abreArchivo(nombre):
    system('clear')
    rutaDatos = "C:\Users\skynet\Desktop\ejercicio_python2\datos"
    #cambia el directorio de trabajo a la ruta indicada
    os.chdir(rutaDatos)
    #abre el archivo
    shapefile = ogr.Open(str(nombre))
 
    if shapefile is None:
        print "El shapefile no existe"
        exit(1)
    else:
        print 'El shapefile '+nombre+' se abrio satisfactoriamente'
    return shapefile

#funcion que devuelve el valor de un pixel:
def getPixelValue(lon, lat):
    #transforma coordenadas x,y a coordenadas pixel
    geotransform = rasterFile.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    pixelWidth = geotransform[1]
    pixelHeight = geotransform[5]
    xOffset = int((lon-originX) / pixelWidth)
    yOffset = int((lat-originY) / pixelHeight)

    #lee los datos del raster en ese punto como un array:
    data = banda.ReadAsArray(xOffset, yOffset, 1, 1)
    valorPixel = data[0,0]
    return valorPixel
    
#abre archivo shape
nombreShape='puntos.shp'
shapefile=abreArchivo(nombreShape)
Vectorlayer = shapefile.GetLayer(0)

#abre archivo raster
nombreRaster= 'EGM08_REDNAP.tif'
rasterFile = gdal.Open(nombreRaster)  #crea objeto gdal-dataset
if rasterFile is None:
    print 'No se pudo abrir: '+nombreRaster
    sys.exit(1)
banda = rasterFile.GetRasterBand(1)    #crea un objeto 'band'

#introduce los datos en el listado
listadoDatos=[]
for i in range(Vectorlayer.GetFeatureCount()):
    feature = Vectorlayer.GetFeature(i) #itera por todas las features del shape
    id = feature.GetField("punto")
    alturaElipsoidal = feature.GetField("altura")
    latitud = feature.GetField("latitud")
    longitud = feature.GetField("longitud")
    geometry = feature.GetGeometryRef()
    ondulacion= getPixelValue(longitud, latitud) 
    alturaOrtometrica=alturaElipsoidal-ondulacion
    listadoDatos.append({'id':id, 'latitud':latitud, 'longitud': longitud, 'altura_elipsoidal':alturaElipsoidal, 'ondulacion':ondulacion,'altura_ortometrica':alturaOrtometrica})
    print id, latitud, longitud, alturaElipsoidal, ondulacion, alturaOrtometrica

#guarda el listado en un archivo de texto:
nombre_archivo='listado.txt' #lo crea en la 'ruta_datos' definida en linea12
archivo=open(nombre_archivo,"w+") #si el archivo no existe lo crea, si existe lo sobreescribe
i=0
archivo.write('id, latitud, longitud, alturaElipsoidal, ondulacion, alturaOrtometrica')
archivo.write("\n")
while i <len(listadoDatos):
    linea=str(listadoDatos[i]['id'])+ ','+str(listadoDatos[i]['latitud'])+','+str(listadoDatos[i]['longitud'])+','+str(listadoDatos[i]['altura_elipsoidal'])+','+str(listadoDatos[i]['ondulacion'])+','+str(listadoDatos[i]['altura_ortometrica'])
    archivo.write(linea)
    archivo.write("\n")
    i =i+1
print 'Archivo '+ nombre_archivo+' creado'
archivo.close()





    
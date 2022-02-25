#Tarea 2: Explorar alternativas de lectura de ficheros
#Libreria con nuestro metodo
#Leyendo documentos zip con dask dentro de la carpeta data.zip
track = dd.read_csv('zip://tracks_norm.csv',  storage_options={'fo': 'data.zip'}, sep=';')
album = dd.read_csv('zip://albums_norm.csv',  storage_options={'fo': 'data.zip'}, sep=';')
artist = dd.read_csv('zip://artists_norm.csv',  storage_options={'fo': 'data.zip'}, sep=';')


#Libreria
import dask.dataframe as dd
import dask.dataframe as dd
import matplotlib.pyplot as plt 

#TIEMPOS CON DASK

#Funcion con el metodo dask
from time import time 

def dask(ruta, columna):
    start = time()
    df = dd.read_csv(f'zip://{ruta}',  storage_options={'fo': 'data.zip'}, sep=';')[columna].compute()
    lineas_read = len(df)
    end = time()
    tiempo_ejecu = end - start
    return tiempo_ejecu, lineas_read



#TIEMPO CON PANDAS
from time import time 
def pandas(rut, colum):
    start = time()
    zf=zipfile.ZipFile(os.path.join(os.getcwd(),'data.zip'))
    read = pd.read_csv(zf.open(rut), sep=';')[colum]
    tamaño_lineas = len(read)
    end = time()
    tiempo_ejecu = end - start
    return tiempo_ejecu, tamaño_lineas, tiempo_ejecu

pandas('artists_norm.csv', 'artist_id')

dask('albums_norm.csv', 'album_id')

#FUNCION PARA GRAFICAR TIEMPOS DE AMBOS METODOS
def lineas_tiempo(x, y, y1):
    '''
    eje de las x : numero de filas leidas
    eje de las y : tiempo de ejecucion 
    '''
    plt.plot(x, y, marker="x",color='r')
    plt.plot(x, y1, marker="o",color='b')
    plt.ylabel(u'Tiempo')
    plt.xlabel(u'Numero de columnas') 
    plt.legend(("tiempo pandas","tiempo dask"))
    plt.show()


#FUNCION PARA GRAFICAR LOS DIFERENTES DATASETS
def graficas_tiempo(archivo, columna, save=False):
    panda = pandas(archivo, columna)
    dk = dask(archivo, columna)
    filas_panda = panda[1]
    tiempo_panda = panda[0]
    tiempo_dask = dk[0]
    lineas_tiempo(filas_panda, tiempo_panda, tiempo_dask)

    if save == False:
        pass
    else:
        plt.savefig('Tiempos.png')
    plt.show()

#criterios de aceptacion 
graficas_tiempo('albums_norm.csv', 'album_id')
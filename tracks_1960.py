#importar librerias
import pandas as pd
df =pd.read_csv(open('/home/yomi/Documentos/PROYECTO GRUPO C/PROYECTO/data_clean.csv'))

def no_lo_se(year_init):
    '''
    artistas que tiene track en cada una de las decadas
    la funcion recibe el año de inicio, final y tiempo determinado
    devolviendo  el artista que obtuvo track en todas las decadas
    '''
    lista = []
    for i in range(year_init, 2010, 10):
        j = i+10
        h = df[(df['release_year'] >= i) & (df['release_year'] <= j)]
        name = h['artist_name'].unique()
        
        print(f"En la decada del año {i} al {j}\n {name} \n")


#criterios de aceptacion
no_lo_se(1960)
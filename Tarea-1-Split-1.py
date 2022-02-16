# TAREA 1 - SPLIT 1 - Catuxa Cerecedo

# Importar librerias
import pandas as pd
import numpy as np
import zipfile
import os

# Definimos la ruta de nuestro archivo .py
path = os.path.dirname(os.path.abspath(__file__))

# Miramos los archivos dentro de la carpeta
with zipfile.ZipFile('data.zip', 'r') as archivos:
    archivos_lista=archivos.namelist()
    #print(archivos_lista)

[i for i in archivos_lista if not i.startswith('__MACOSX/')]

# Abrimos con pandas
zf=zipfile.ZipFile(os.path.join(path, 'data.zip'))
albums=pd.read_csv(zf.open(archivos_lista[0]), sep=';')
artistas=pd.read_csv(zf.open(archivos_lista[1]), sep=';')
tracks=pd.read_csv(zf.open(archivos_lista[2]), sep=';')

# Corregir los nombres de los artistas
artistas['name'] = artistas['name'].str.title()
#artistas['name'].unique()

# Rellenar los valores Na de popularity de los tracks
tracks['popularity'] = np.where(np.isnan(tracks['popularity']), np.mean(tracks['popularity']), tracks['popularity'])
#tracks['popularity'].isnull().sum()

# Cambio de nombres de columnas que se llaman igual.
# Dejamos con el mismo nombre las columnas a concatenar.
tracks = tracks.rename(columns={'name':'track_name',
                        'popularity': 'popularity_track'})
albums = albums.rename(columns={'name':'album_name',
                        'popularity': 'popularity_album'})
artistas = artistas.rename(columns={'name':'artist_name',
                        'popularity': 'popularity_artist'})

# Concatenación de tablas
df1 = tracks.merge(albums, on='album_id')
df1 = df1.rename(columns={'artist_id_x':'artist_id'})
df2 = df1.merge(artistas, on='artist_id')
df2.drop(['artist_id_y'], axis = 'columns', inplace=True)

# Borramos duplicados
df2.drop_duplicates()

# Criterios de aceptación
print(f'El número de tracks totales {df2.shape[0]} y el número de columnas es {df2.shape[1]}')
print(f'El número de tracks sin un valore de popularity es {len(df2[pd.isnull(df2.popularity_track)])}')

# Guardamos el nuevo csv
df2.to_csv(os.path.join(os.getcwd(), 'data_clean.csv'), index = True)

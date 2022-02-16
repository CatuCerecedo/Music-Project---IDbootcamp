# TAREA 2 - SPLIT 1 - Catuxa Cerecedo

# Importar librerias
import pandas as pd
import numpy as np
from datetime import date
import os

# Definimos la ruta de nuestro archivo .py
path = os.path.dirname(os.path.abspath(__file__))

# Importar la base de datos
df = pd.read_csv(os.path.join(path, 'data_clean.csv'))

# Función para contar los tracks que hay de un grupo
def which_artist(name):
    '''
    Number of artist tracks
    
    input:
        str: artist name

    output:
        int: number of tracks
    '''
    name = name.title()
    return len(df[df['artist_name'] == name])

# Función para contar los tracks que contienen una palabra específica 
def searching(word):
    '''
    Number of tracks that have word in the name
    
    input:
        str: word to search

    output:
        int: number of tracks
    '''
    word1 = word.lower()
    word2 = word.title()
    n1 = len(df[df['track_name'].str.contains(word1)]) 
    n2 = len(df[df['track_name'].str.contains(word2)]) 
    return n1 + n2

# Función para contar los tracks en un periodo de tiempo
def year_tracks(year_start, year_end):
    '''
    Number of tracks released in a period of time

    input:
        year_start(int)
        year_end(int)

    output
    '''
    return len(df[(df['release_year'] >= year_start) & (df['release_year'] <= year_end)])

# Función para conocer la canción más popular en los últimos x años
def popularity_year(n_year):
    '''
    Most popular track of the last n years

    input:
        n_year(int): years to subtract from the current year

    result:
        str: track name
    '''
    current_year = date.today().year
    pass_year = current_year - n_year
    df2 = df[df['release_year'] >= pass_year]
    most_popular = max(df2.popularity_track)
    return df2['track_name'][df2['popularity_track'] == most_popular]


# Soluciones a las preguntas
print('¿Cuántos tracks hay del artista Radiohead?')
print(f"{which_artist('radiohead')} tracks\n")

print('¿Cuántos tracks contienen la palabra _police_ en el título?')
print(f"{searching('police')} tracks\n")

print('¿Cuántos tracks son de álbumes publicados en la década del 1990?')
print(f"{year_tracks(1990, 1999)} tracks\n")

print('¿Cuál es la track con más popularidad de los últimos 10 años?')
print(f"El track con mayor popularidad se llamada {popularity_year(10)}\n")

print('¿Qué artistas tienen tracks en cada una de las décadas desde el 1960?')

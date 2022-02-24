# TAREA 4 - SPLIT 1 

# Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Función para buscar y cargar archivo en el directorio
def searching_file(filename):
    '''
    Search the file in the directory and save the path

    Arg:
        filename(str): file name

    Output:
        str: path of file
    '''
    for root, dir, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
        if filename in files:
            path=os.path.join(root, filename)
    df=pd.read_csv(path)
    return df


# Calcular estadísticos de cualquier feature de cualquier artista
def main_stats_artist(df, feature, name=None):
    '''
    Calcula el mínimo la media y el máximo de cualquies feature seleccionando un artista
    '''
    if name!=None:
        name = name.title()
        df2 = df.loc[df['artist_name'] == name]
    else:
        df2 = df
    
    max_value=df2[feature].max()
    min_value=df2[feature].min()
    average_value=df2[feature].mean()

    return {'max_value': max_value, 'average_value':average_value, 'min_value':min_value}

# Función para crear barplot de la media
def plot_album_mean(df, feature, name=None, save=False):

    # Dependiendo si es para toda la tabla o un artista
    if name == None:
        df_artist=df
    else:
        name = name.title()
        df_artist=df[df['artist_name'] == name]

    # Creamos el plot
    plt.figure(figsize=(10, 10))
    sns.barplot(y="album_name", x=feature, data=df_artist, estimator=np.mean, ci=85, capsize=.2, color='lightblue')

    # Dpendiendo de si se quiere guardar
    if save == False:
        pass
    else:
        plt.savefig('Artist_mean_barplots.png', facecolor='white')

    plt.show()

# Criterios de aceptación
df=searching_file('data_clean.csv')
p=main_stats_artist(df, 'energy', 'Metallica')

# Mostrar por pantalla un comentario con las estadísticas básicas de A.
print(f'Estadísticos básicos de Metallica\n {p}')

# Mostrar por pantalla la gráfica generada en B.
plot_album_mean(df, feature='danceability', name='coldplay', save=True)

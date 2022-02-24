# TAREA 5 - SPLIT 2 

# Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Función para buscar archivo en el directorio
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

# Definir la función para la hacer plot
def histogram_artist(df, feature, name=None, save=False):
    '''
    Plot de dos histogramas de un feature numérico de un artísta específico
    input:
        feauture (str): nombre de la audio feature que se quiere analizar
        name (str): Optional. Nombre del artista.
        save (boolean). If true, save the plot. Default False.
    
    '''
    if name == None:
        df_artist=df
    else:
        name = name.title()
        df_artist=df[df['artist_name'] == name]

    # Creamos multiples subplots en uno
    fig, axes = plt.subplots(1,2, figsize=(15, 5))
    fig.suptitle('Histogramas')

    # Histograma de frecuencias
    sns.histplot(x=df_artist[feature], stat="count", bins=10, edgecolor='black', ax=axes[0])
    axes[0].set_title('a) Frecuencias')

    # Histograma de densidades
    sns.histplot(x=df_artist[feature], stat="density", bins=10, edgecolor='black', ax=axes[1])
    axes[1].set_title('b) Densidades de probabilidad')

    if save == False:
        pass
    else:
        plt.savefig('histograms.png', facecolor='white')

    plt.show()
    
# Cirterio de aceptación
df=searching_file('data_clean.csv')
histogram_artist(df, 'acousticness', 'Ed Sheeran', save=False)

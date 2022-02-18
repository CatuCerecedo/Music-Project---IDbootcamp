# TAREA 5 - SPLIT 2 

# Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Definimos la ruta de nuestro archivo .py
path = os.path.dirname(os.path.abspath(__file__))

# Importar la base de datos
df = pd.read_csv(os.path.join(path, 'data_clean.csv'))

# Definir la función para la hacer plot

def histogram_artist(feature, name=None, save=False):
    '''
    Plot de dos histogramas de un feature numérico de un artísta específico
    '''
    if name == None:
        df_artist=df
    else:
        df_artist=df[df['artist_name'] == name]

    # Creamos multiples subplots en uno
    fig, axes = plt.subplots(1,2, figsize=(15, 5))
    fig.suptitle('Histogramas')

    x = df[feature]

    # Histograma de frecuencias
    sns.histplot(x=df_artist.acousticness, stat="count", bins=10, edgecolor='black', ax=axes[0])
    axes[0].set_title('a) Frecuencias')

    # Histograma de densidades
    sns.histplot(x=df_artist.acousticness, stat="density", bins=10, edgecolor='black', ax=axes[1])
    axes[1].set_title('b) Densidades de probabilidad')

    if save == False:
        pass
    else:
        plt.savefig('histograms.png', facecolor='white')
    
    return plt.show()

# Cirterio de aceptación
histogram_artist('acousticness', 'Ed Sheeran', save=False)

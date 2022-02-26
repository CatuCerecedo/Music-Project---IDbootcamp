#densidad de probabilidad de dos artistas histogramas

# Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df =pd.read_csv(open('/home/yomi/Documentos/PROYECTO GRUPO C/PROYECTO/data_clean.csv'))
def compar_artis(artist_1, artist_2, ene, save=False):
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.suptitle('Histogramas')

    #artistas en funcion de energy
    a1= df[df['artist_name'] == artist_1][ene]
    a2= df[df['artist_name'] == artist_2][ene]
    bins = np.linspace(-10, 10, 60)
    #grafico artista 
    plt.hist(a1, bins,alpha = 0.7, label='astist 1', edgecolor='black', color='orange')
    plt.hist(a2, bins,alpha = 0.5, label='artist 2', color='#288A92', edgecolor='black')
    plt.legend(loc='upper left')
    plt.xlabel('Energy')
    plt.ylabel('Density')

    if save == False:
        pass
    else:
        plt.savefig('Artistas histogramas.png', facecolor='white')

#criterios de aceptacion

compar_artis('Adele', 'Extremoduro', 'energy')

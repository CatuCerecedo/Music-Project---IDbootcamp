#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime as dt
import pandas as pd
import requests


# In[2]:


#Ejemplo: Búsqueda de todos los videos de un artista
# Es una consulta, por lo que utilizamos el método GET de la API http. Los más conocidos son HTTP GET, POST, PUT, DELETE, PATCH.
# En este caso, el único parámetro que necesita es el id del artista del cuál queremos obtener los vídeos. En este caso es 112024
# Para hacer la consulta utilizamos la librería "requests" de python y el método "get"
api_videos = "https://theaudiodb.com/api/v1/json/2/mvid.php?i=112024"
response_videos = requests.get(api_videos)


# In[3]:


response_videos.status_code


# In[4]:


response_videos.json()


# In[5]:


#Otro ejemplo 
api_album = "https://theaudiodb.com/api/v1/json/2/search.php?s=coldplay"
response_albums_coldplay = requests.get(api_album)


# In[6]:


response_albums_coldplay.status_code


# In[7]:


response_albums_coldplay.json()


# In[ ]:





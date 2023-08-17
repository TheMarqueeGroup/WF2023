# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:48:32 2022

@author: bogda
"""

import requests
import pandas as pd

#%% FRED Scrape Directly
# https://fred.stlouisfed.org/series/GDP
# test = 'https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=BA3M&scale=left&cosd=1980-06-04&coed=2000-06-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2000-06-01&line_index=1&transformation=lin&vintage_date=2022-11-25&revision_date=2022-11-25&nd=1941-01-01'
test = 'https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDP&scale=left&cosd=1947-01-01&coed=2023-04-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-08-15&revision_date=2023-08-15&nd=1947-01-01'
stlFed = pd.read_csv(test)

#%% FRED API
#Working API
    #https://fred.stlouisfed.org/docs/api/fred/

# https://fred.stlouisfed.org/docs/api/fred/series_observations.html

#Wrapper for FRED:
    # https://github.com/mortada/fredapi
    # https://anaconda.org/conda-forge/fredapi

#%%% FRED Series Observations
# url = 'https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&api_key=2080f5d1960f074428e503fd03e71960&file_type=json&frequency=d'
rootURL = 'https://api.stlouisfed.org/fred/series/observations?series_id='
# seriesID = 'DGS10'
seriesID = 'T10Y3M'
apiKey = '&api_key=2080f5d1960f074428e503fd03e71960' #please change this to your API KEY
fileType = '&file_type=json'
freq = '&frequency=d' #change d to m, y, etc.

url= rootURL + seriesID + apiKey + fileType + freq

req = requests.get(url)
data = req.json()
df = pd.DataFrame(data['observations'])
df.to_csv('Output/'+seriesID+'.csv')
#%%% Info about the Series
rootURL = 'https://api.stlouisfed.org/fred/series?series_id='
url= rootURL + seriesID + apiKey + fileType
req = requests.get(url)
data = req.json()
seriesName = data['seriess'][0]['title']
print(seriesID, seriesName)









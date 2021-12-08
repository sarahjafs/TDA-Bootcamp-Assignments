# TDA-Bootcamp-Assignments
# The repository for Sarah's Bootcamp assignments
# importing pandas, numpy and matplotlib, giving them aliases, pd, np, and plt respectively
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# importing the relevant data file to the code
# earthquakes is my data file name
earthquakes = pd.read_csv('all_month.csv')
earthquakes
# creating a pandas profile to assess what correlations there are that I can look into further
from pandas_profiling import ProfileReport
ProfileReport(earthquakes)
# having a look at the earthquake file statistics such as count of entries, mean, standard deviation, centiles
earthquakes.describe()
# checking to see blanks in the data
earthquakes.isnull().sum()
# filtering the earthquakes data by the columns of time, latitude, longitude, depth and magnitude
# alias given for this filter is 'efil'
efil = earthquakes[['time','latitude','longitude','depth','mag']]
efil
#earthquakes filtered
# filtering further to give only values with a magnitude higher than 3 since that is a significant magnitude
# this is called 'efilmag'
efilmag = efil[efil['mag']>=3]
efilmag
# plotting efilmag
%matplotlib inline
fig,ax = plt.subplots()
efilmag.plot(kind = 'scatter', x = 'mag' , y = 'depth', alpha = 0.5, color = 'pink', ax = ax)
#alpha = 0.5 will give density
# filtering a specfic longitude (>20) and latitutde (>30)
elonlatfil = efilmag[(efil['latitude']>20)&(efil['latitude']>30)]
elonlatfil
#places with deep earthquakes are likely to be closer to the tectonic plates. It is worth looking into longitude&latitude correlation with tectonic plates. 
earthquake_filtered_places_longlat = earthquake[['place','latitude','longitude','mag']]
earthquake_filtered_places_longlat
# plotting a scatter grapth of efilmag with weighted points to show magnitude
%matplotlib inline
fig,ax = plt.subplots()
efilmag.plot(kind = 'scatter', x = 'longitude', y = 'latitude', alpha = 0.5, 
color = 'pink', ax = ax)
# importing more fun visual installations for this specific dataset visualisation
pip install geopandas
pip install geoplot
pip install folium
import geoplot
import geopandas
import seaborn as sns
import folium
from folium import Choropleth
from folium.plugins import HeatMap
import datetime
np.random.seed(0)
# mapping tectonic plates on the folium map (!)
tectonic = folium.Map(tiles='cartodbpositron',zoom_start=5)
tectonic
# creating a seaborn with weighted magnitudes, this looks good
sns.relplot(data = efilmag, x="longitude", y="latitude", hue="mag", size="mag", hue_norm=(-1,7))
#overlaying the map of longitude and latitude on top of a map, and earthquakes of high magnitude on top.
geometry = geopandas.points_from_xy(efilmag.longitude, efilmag.latitude)
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
%matplotlib inline
fig,ax = plt.subplots()
world.plot(ax=ax, alpha=0.4, color='gray')
#shows plates
data.plot(kind = 'scatter', x = 'lon', y = 'lat',ax=ax, s=1, color='gray')
efilmag.plot(kind = 'scatter', x = 'longitude', y = 'latitude', alpha = 0.5, 
color = '#FF0099', ax = ax)
tectonic = folium.Map(tiles="cartodbpositron", zoom_start=5)
%matplotlib inline
fig,ax = plt.subplots()
efilmag.plot(kind = 'scatter', x = 'longitude', y = 'latitude', alpha = 0.5, 
color = 'pink', ax = ax)
sns.relplot(data = efilmag, x="longitude", y="latitude", hue="mag", size="mag", hue_norm=(-1,7))
fig, ax = plt.subplots()
plt.scatter(earthquake_filtered_places_longlat.longitude, earthquake_filtered_places_longlat.latitude, alpha = .8,c = earthquake_filtered_places_longlat.mag, cmap = 'seismic')
cbar = plt.colorbar()
earthquake['time']=pd.to_datetime(earthquake['time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
earthquake['time']
earthquake
earthquake.boxplot('mag')
fg,ax=plt.subplots()
earthquake.boxplot(column=['mag','depth'])
data = pd.read_csv("all.csv.xls")
#dropping columns with missing values
missing_values_columns = [col for col in data.columns
                     if data[col].isnull().any()]
data = data.drop(missing_values_columns, axis=1)
data.head()
data.plot(kind = 'scatter', x = 'lon', y = 'lat')

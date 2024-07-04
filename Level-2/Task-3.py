import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas 
from geodatasets import get_path
import folium
from folium.plugins import HeatMap

url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)

#Task: Geographic Analysis
'''Plot the locations of restaurants on a
   map using longitude and latitude
   coordinates.'''

print(df[["Longitude","Latitude"]])

gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
)

print(gdf.head())

world = geopandas.read_file(get_path("naturalearth.land"))
ax = world.plot(color='white', edgecolor='black')
gdf.plot(ax=ax, marker='o', color='red', markersize=5)

plt.show()

'''Identify any patterns or clusters of
   restaurants in specific areas.'''
world_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=1, height = '100%' , width = '100%')

heat_marker = [[row['Latitude'], row['Longitude']] for i, row in df.iterrows()]
HeatMap(heat_marker, radius=10).add_to(world_map)

world_map

world_map.save("heat_map.html")
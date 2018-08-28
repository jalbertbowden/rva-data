import csv
#from pyproj import Proj

#p = Proj(init='epsg:3359')
#lon, lat = p(21109260., 7382520., inverse=True)
#p = Proj(init='epsg:4326')
#lon, lat = p(11776158.34,3725544.364, inverse=True)
#print lon, lat


import pyproj
wgs84 = pyproj.Proj("+init=EPSG:4326")
va_state = pyproj.Proj("+init=EPSG:2284", preserve_units=True)
xx = pyproj.transform(va_state, wgs84, 11776158.34,3725544.364)
print xx
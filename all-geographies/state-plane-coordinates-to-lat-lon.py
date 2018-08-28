import csv
from pyproj import Proj, transform


inProj = Proj(init='epsg:2284')
outProj = Proj(init='epsg:4326')


#x1,y1 = -11705274.6374,4826473.6922
#x2,y2 = transform(inProj,outProj,x1,y1)
#print x2,y2

f = open("all-geographies-richmond-virginia-all-cases-fc.csv")
reader = csv.DictReader(f)
for row in reader:
  # Add your own logic here
  # ...for example, printing out data in the column "Name" for each row would be:
  x1,y1 = row["X_COORD"],row["Y_COORD"]
  #print(row["X_COORD"] + " " + row["Y_COORD"])
  x2,y2 = transform(inProj,outProj,x1,y1)
  print x2,y2
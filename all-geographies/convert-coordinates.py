import pyproj
import csv


wgs84 = pyproj.Proj("+init=EPSG:4326")
#ny_state = pyproj.Proj("+init=EPSG:2263")
va_state = pyproj.Proj(init='epsg:2284', preserve_units=True)
result = pyproj.transform(va_state, wgs84, 11776158.34, 3725544.364)

csvfile = "all-geographies-richmond-virginia-all-cases-fc-wsg84-coordinates.csv"
newData = []

f = open("all-geographies-richmond-virginia-all-cases-fc.csv")
reader = csv.DictReader(f)
for row in reader:
  # Add your own logic here
  # ...for example, printing out data in the column "Name" for each row would be:
  x1,y1 = row["X_COORD"],row["Y_COORD"]
  #print x1,y1
  #print(row["X_COORD"] + " " + row["Y_COORD"])
  x2,y2 = pyproj.transform(va_state, wgs84,x1,y1)
  #print x2,y2

  newData.extend([x2,y2])


with open(csvfile, "w") as output:
  writer = csv.writer(output, lineterminator='\n')
  writer.writerow([newData]) 
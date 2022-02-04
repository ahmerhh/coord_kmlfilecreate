import shapefile
import simplekml
import os
from simplekml import Kml

#(Variable file name: entered by user at runtime)
filename = input("Input file location: ")
#Reading shapefile
shape = shapefile.Reader(filename)
file_save_name = input("Enter file name: ")
file_des = input("File description: ")


#KML
kml = simplekml.Kml()
kml.document.name = file_save_name

emptyCoord = []
for x in range(len(shape)):
    feature = shape.shapeRecords()[x]
    first = feature.shape.__geo_interface__
    coordinates = list(first.values())[1]
    emptyCoord.append(coordinates)


    

lin = kml.newlinestring(name=kml.document.name, description=file_des, coords=emptyCoord)

kml.save(os.path.splitext(file_save_name)[0] + ".kml")
import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur = db.cursor() 

limit = 20000

query = "SELECT * FROM cdr LIMIT " + str(limit)

cur.execute(query)

listOfTrafficVolumes_dataVolumeGPRSDownlink = []
listOfTrafficVolumes_dataVolumeGPRSUplink = []
duration = []

for row in cur.fetchall() :
    listOfTrafficVolumes_dataVolumeGPRSDownlink.append(row[0])
    listOfTrafficVolumes_dataVolumeGPRSUplink.append(row[3])
    duration.append(row[22])


listOfTrafficVolumes_dataVolumeGPRSDownlink = [int(i) for i in listOfTrafficVolumes_dataVolumeGPRSDownlink]
listOfTrafficVolumes_dataVolumeGPRSUplink = [int(i) for i in listOfTrafficVolumes_dataVolumeGPRSUplink]
duration = [int(i) for i in duration]

from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pylab.figure()
ax = Axes3D(fig)

x = listOfTrafficVolumes_dataVolumeGPRSDownlink
y = listOfTrafficVolumes_dataVolumeGPRSUplink
z = duration


ax.scatter(x, y, z)

pyplot.show()
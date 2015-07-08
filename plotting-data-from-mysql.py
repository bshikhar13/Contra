import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="bshikhar13", # your password
                      db="cdr") # name of the data base

cur = db.cursor() 


cur.execute("SELECT * FROM cdr LIMIT 30000")

listOfTrafficVolumes_dataVolumeGPRSDownlink = []
listOfTrafficVolumes_dataVolumeGPRSUplink = []

for row in cur.fetchall() :
    listOfTrafficVolumes_dataVolumeGPRSDownlink.append(row[0])
    listOfTrafficVolumes_dataVolumeGPRSUplink.append(row[3])

listOfTrafficVolumes_dataVolumeGPRSDownlink = [int(i) for i in listOfTrafficVolumes_dataVolumeGPRSDownlink]
listOfTrafficVolumes_dataVolumeGPRSUplink = [int(i) for i in listOfTrafficVolumes_dataVolumeGPRSUplink]


import numpy as np
import matplotlib.pyplot as pp
val1 = 0
val2 = 0

pp.plot(listOfTrafficVolumes_dataVolumeGPRSDownlink,listOfTrafficVolumes_dataVolumeGPRSUplink,'ro')

xl = pp.xlabel('DownlinkDate')
yl = pp.ylabel('UpLink Data')
ttl = pp.title('Downlink GPRS data vs UPlink GPRS Data')

grd = pp.grid(True)



pp.show()
import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur = db.cursor() 


cur.execute("SELECT * FROM cdr LIMIT 100000")

listOfTrafficVolumes_dataVolumeGPRSDownlink = []
listOfTrafficVolumes_dataVolumeGPRSUplink = []

for row in cur.fetchall() :
    listOfTrafficVolumes_dataVolumeGPRSDownlink.append(row[0])
    listOfTrafficVolumes_dataVolumeGPRSUplink.append(row[3])

listOfTrafficVolumes_dataVolumeGPRSDownlink = [int(i) for i in listOfTrafficVolumes_dataVolumeGPRSDownlink]
listOfTrafficVolumes_dataVolumeGPRSUplink = [int(i) for i in listOfTrafficVolumes_dataVolumeGPRSUplink]


import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
from scipy import stats
import seaborn as sns
sns.set(color_codes=True)
import pylab as plt


val1 = 0
val2 = 0

pp.plot(listOfTrafficVolumes_dataVolumeGPRSDownlink,listOfTrafficVolumes_dataVolumeGPRSUplink,'ro')

xl = pp.xlabel('DownlinkDate')
yl = pp.ylabel('UpLink Data')
ttl = pp.title('Downlink GPRS data vs UPlink GPRS Data')

x = listOfTrafficVolumes_dataVolumeGPRSDownlink
y = listOfTrafficVolumes_dataVolumeGPRSUplink

grd = pp.grid(True)

Z = []





pp.show()
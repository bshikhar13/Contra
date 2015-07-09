import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur = db.cursor() 

limit = 500

query = "SELECT DISTINCT servedIMSI FROM cdr LIMIT " + str(limit)

cur.execute(query)

listOfTrafficVolumes_dataVolumeGPRSDownlink = []
listOfTrafficVolumes_dataVolumeGPRSUplink = []
duration = []
frequency_IMSI = []
for row in cur.fetchall() :
	IMSI = row[0]
	#print IMSI
	if IMSI :
		innercur = db.cursor()
		innerquery = "SELECT count(*) FROM cdr WHERE servedIMSI = " + IMSI + " LIMIT 0,10000000"
		#print IMSI
		#print innerquery
		innercur.execute(innerquery)
		for innerrow in innercur.fetchall():
			#print "YOYOYO"
			frequency_IMSI.append(innerrow[0])
			result = IMSI + "  :  "+ str(innerrow[0])
			#print result



frequency_IMSI = [int(i) for i in frequency_IMSI]



import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
print frequency_IMSI
import seaborn as sns

tem = np.mean(frequency_IMSI)

print (frequency_IMSI)
plt.hist(frequency_IMSI,bins = 500)
plt.title("Number of SIMs vs Activity")
plt.xlabel("Activity")
plt.ylabel("Number of SIMs")
plt.show()

sns.set(color_codes=True)
e = sns.distplot(frequency_IMSI,hist=False, rug=True);	
print e

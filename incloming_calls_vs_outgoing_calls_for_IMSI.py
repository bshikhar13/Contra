import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur = db.cursor() 

limit = 3000

query = "SELECT DISTINCT IMSI_number FROM cdr_voice LIMIT " + str(limit)

cur.execute(query)

MOCA = []
MTCA = []

counter = 1
for row in cur.fetchall() :
	IMSI = row[0]
	#print IMSI
	if IMSI :
		innercur_MOCA = db.cursor()
		innercur_MTCA = db.cursor()
		
		innerquery_MOCA = "SELECT count(*) FROM cdr_voice WHERE LongType = 'Mobile Originated Call Attempt' AND IMSI_number = " +str(IMSI) + " LIMIT 0,1000000"
		innerquery_MTCA = "SELECT count(*) FROM cdr_voice WHERE LongType = 'Mobile Terminated Call Attempt' AND IMSI_number = " +str(IMSI) + " LIMIT 0,1000000"
		#print IMSI
		#print innerquery
		innercur_MOCA.execute(innerquery_MOCA)
		innercur_MTCA.execute(innerquery_MTCA)

		for innerrow_MOCA in innercur_MOCA.fetchall():
			for innerrow_MTCA in innercur_MTCA.fetchall():
				#print str(counter) + " :: " + IMSI + " : "+ str(innerrow_MOCA[0]) + " : " + str(innerrow_MTCA[0])
				MOCA.append(innerrow_MOCA[0])
				MTCA.append(innerrow_MTCA[0])
			
		counter = counter + 1	
#print MOCA
#print MTCA
print counter
x = MOCA
y = MTCA

import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
from scipy import stats
import seaborn as sns
sns.set(color_codes=True)
import pylab as plt



pp.plot(x,y,'go')
pp.plot([0, 0], [40, 40])
xl = pp.xlabel('Outgoing Calls')
yl = pp.ylabel('Incoming Calss')
ttl = pp.title('Outgoing calls vs Incoming calls ')


grd = pp.grid(True)
pp.show()

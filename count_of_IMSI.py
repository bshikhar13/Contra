import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur = db.cursor() 

limit = 50

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
			print result



	


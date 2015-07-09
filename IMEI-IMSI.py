import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur = db.cursor() 

limit = 20
#same IMSI with different IMEI
#query = "SELECT t1.IMSI_number, t1.IMEI_number, t2.IMSI_number, t2.IMEI_number FROM cdr_voice as t1 JOIN cdr_voice as t2 ON t1.Type = '0' and t2.Type = '0' and t1.IMSI_number != '' and t1.IMEI_number != '' and t2.IMSI_number != '' and t2.IMEI_number != '' and t1.IMSI_number = t2.IMSI_number and t1.IMEI_number != t2.IMEI_number LIMIT " + str(limit)

#same IMEI with different IMSI
query = "SELECT t1.IMSI_number, t1.IMEI_number, t2.IMSI_number, t2.IMEI_number FROM cdr_voice as t1 JOIN cdr_voice as t2 ON t1.Type = '0' and t2.Type = '0' and t1.IMSI_number != '' and t1.IMEI_number != '' and t2.IMSI_number != '' and t2.IMEI_number != '' and t1.IMSI_number != t2.IMSI_number and t1.IMEI_number = t2.IMEI_number LIMIT " + str(limit)

cur.execute(query)

counter = 1
for row in cur.fetchall() :
	#print len(row)
	#print row
	print row[0] + " : " + row[1] + " : " + row[2] + " : " + row[3]

import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur = db.cursor() 

limit = 240000
#same IMSI with different IMEI
#query = "SELECT t1.IMSI_number, t1.IMEI_number, t2.IMSI_number, t2.IMEI_number FROM cdr_voice as t1 JOIN cdr_voice as t2 ON t1.Type = '1' and t2.Type = '1' and t1.IMSI_number != '' and t1.IMEI_number != '' and t2.IMSI_number != '' and t2.IMEI_number != '' and t1.IMSI_number = t2.IMSI_number and t1.IMEI_number != t2.IMEI_number LIMIT " + str(limit)

#same IMEI with different IMSI
query = "SELECT t1.IMSI_number, t1.IMEI_number, t2.IMSI_number, t2.IMEI_number FROM cdr_voice as t1 JOIN cdr_voice as t2 ON ((t1.Type = '1' and t2.Type = '1') or (t1.Type = '0' and t2.Type = '0') ) and t1.IMSI_number != '' and t1.IMEI_number != '' and t2.IMSI_number != '' and t2.IMEI_number != '' and t1.IMSI_number != t2.IMSI_number and t1.IMEI_number = t2.IMEI_number LIMIT " + str(limit)

cur.execute(query)

import collections
D = collections.defaultdict(list)

def hashIMEI_IMSI (a,b):
	D[a].append(b)

counter = 1
for row in cur.fetchall() :
	#print len(row)
	#print row
	#print row[0] + " : " + row[1] + " : " + row[2] + " : " + row[3]
	hashIMEI_IMSI(row[1],row[0])


#print D
for k,v in D.items():
	v = list(set(v))
	print k + " :: " + str(len(v))
	st = ""
	for v1 in v :
		st = st + v1 + "  "
	print st
	print "\n"	
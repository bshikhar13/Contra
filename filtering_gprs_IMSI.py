import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 

cur_cdr = db.cursor() 
cur_cdr_voice = db.cursor() 

limit_cdr = 200000
limit_cdr_voice = 200000

query_cdr = "SELECT IMSI_number from cdr_voice LIMIT " + str(limit_cdr)
query_cdr_voice = "SELECT servedIMSI from cdr LIMIT "+ str(limit_cdr_voice)


cur_cdr.execute(query_cdr)
cur_cdr_voice.execute(query_cdr_voice)

cdr_list = []
cdr_voice_list = []

import collections
D = collections.defaultdict(list)

def hashIMEI_IMSI (a,b):
	D[a].append(b)

count = 0
for row in cur_cdr.fetchall() :
	imsinumber = row[0] 
	cdr_list.append(imsinumber)

for row in cur_cdr_voice.fetchall() :
	imsinumber = row[0] 
	cdr_voice_list.append(imsinumber)



cdr_list = list(set(cdr_list))
cdr_voice_list = list(set(cdr_voice_list))


print "Unique SIMs who use Internet : " + str(len(cdr_list))
print "Unique SIMs who use voice calling : " + str(len(cdr_voice_list))

suspiciouslist = list(set(cdr_voice_list)-set(cdr_list))

print "Suspicios SIMs on the basis of not using Internet : " + str(len(suspiciouslist))
print "UnSuspicios SIMs : " + str(len(cdr_voice_list)-len(suspiciouslist))

suspiciouslist.append('Shikhar')
print suspiciouslist
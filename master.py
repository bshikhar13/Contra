from filtering_gprs_IMSI import suspiciouslist as a
from SMS_USSD import unsuspicios as b

print b
print a

for a1 in a:
	for b1 in b:
		if a1!=b1:
			print "yoyo"

			

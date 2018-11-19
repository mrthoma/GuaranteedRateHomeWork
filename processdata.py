import sys
import traceback
import json
from   datetime    import datetime
import re
from   operator    import itemgetter
from   collections import OrderedDict
flist = []
plist = []



def process_input(line):

	try:
		#check if the fields are good
		fields = re.split(r'[ ,|]+', line.replace('\n', ''))
	except:
		#if not good: put it on the flist
		flist.append(line.replace('\n', ''))
		
	if len(fields) > 5:
		flist.append(line.replace('\n', ''))
		raise ValueError("TOO MANY FIELDS")

	elif len(fields) < 5:
		flist.append(line.replace('\n', ''))
		raise ValueError("NOT ENOUGH FIELDS")

	else:
		LastName  = fields[0]
		FirstName = fields[1]
		Gender    = fields[2]
		FavColor  = fields[3]
		DOB       = fields[4]
		DOBSTRIP  = str(datetime.strptime(DOB,'%d/%m/%Y').date())


		plist.append({"lastname": LastName, "firstname": FirstName,  "dob": DOBSTRIP, "favcolor": FavColor, "gender": Gender})

		return(plist,flist)

def get_order_gender():
	return (sorted(plist, key=itemgetter('gender', 'lastname')))

def get_order_dob():
	return (sorted(plist, key=itemgetter('dob')))
	#plist.sort(key=lambda item:item[datetime.strptime('dob', '%d/%m/%Y').date()])
	#return(plist)

def get_order_reverse_lastname():
	return (sorted(plist, key=itemgetter('lastname'),reverse = True))

def get_flist():
	return flist

def get_failcount():
	return len(flist)

def get_recordcount():
	return len(plist)
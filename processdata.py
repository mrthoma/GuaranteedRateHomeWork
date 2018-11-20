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
		#check if using the proper delimiter
		fields     = re.split(r'[ ,|]+', line.replace('\n', ''))
		#check if date is in the right format
		dateformat = str(datetime.strptime(fields[4],'%m/%d/%Y').date())
	except:
		#if failed, put it on the flist for the user to review
		flist.append(line.replace('\n', ''))


	if len(fields) > 5:
		flist.append(line.replace('\n', ''))
		raise ValueError("TOO MANY FIELDS")

	elif len(fields) < 5:
		flist.append(line.replace('\n', ''))
		raise ValueError("NOT ENOUGH FIELDS")

	else:
		#Get the rest of the fields in there
		LastName  = fields[0]
		FirstName = fields[1]
		Gender    = fields[2]
		FavColor  = fields[3]
		DOB       = dateformat

		plist.append({"lastname": LastName, "firstname": FirstName,  "dob": DOB, "favcolor": FavColor, "gender": Gender})

		return(plist,flist)

def get_order_gender():
	return (sorted(plist, key=itemgetter('gender', 'lastname')))

def get_order_dob():
	return (sorted(plist, key=itemgetter('dob')))

def get_order_reverse_lastname():
	return (sorted(plist, key=itemgetter('lastname'),reverse = True))

def get_flist():
	return flist

def get_failcount():
	return len(flist)

def get_recordcount():
	return len(plist)
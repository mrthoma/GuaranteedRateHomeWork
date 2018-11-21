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
		#check if using the proper delimiter and can split it into fields
		fields = re.split(r'[ ,|]+', line.replace('\n', ''))

	except:
		#if failed, put it on the flist for the user to review
		flist.append(line.replace('\n', ''))
		raise ValueError("Either not enough fields... or date is in the wrong format")

	if len(fields) > 5:
		#do you have too many fields?
		flist.append(line.replace('\n', ''))
		raise ValueError("TOO MANY FIELDS")

	elif len(fields) < 5:
		#do you have too few fields?
		flist.append(line.replace('\n', ''))
		raise ValueError("NOT ENOUGH FIELDS")

	try:
		#now see if the date is in the right format
		dateformat = datetime.strptime(fields[4],'%m/%d/%Y').strftime('%m/%d/%Y')
	except:
		flist.append(line.replace('\n', ''))
		raise ValueError("DATE NOT IN MM/DD/YYYY")

	#alls good, lets go!
	LastName  = fields[0]
	FirstName = fields[1]
	Gender    = fields[2]
	FavColor  = fields[3]
	DOB       = dateformat

	plist.append({"lastname": LastName, "firstname": FirstName,  "dob": DOB, "favcolor": FavColor, "gender": Gender})

	return(plist,flist)

def get_order_gender():
	return (sorted(plist, key=itemgetter('gender', 'lastname')))

def sort_dob(item):
	return (datetime.strptime(item['dob'], '%m/%d/%Y'))

def get_order_dob():
	return (sorted(plist, key=sort_dob))

def get_order_reverse_lastname():
	return (sorted(plist, key=itemgetter('lastname'),reverse = True))

def get_flist():
	return flist

def get_failcount():
	return len(flist)

def get_recordcount():
	return len(plist)
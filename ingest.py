#!/bin/python3
###################################################
#Guaranteed Rate Dev Homework
#Mike Thoma 11/11/2018

###################################################
#REQUIREMENTS
###################################################
import sys
import re
import json
from pprint import pprint
from operator import itemgetter

###################################################
#VARIABLES
###################################################
userfile    = sys.argv[-1]

###################################################
#FUNCTIONS
###################################################
def check_arguments():
	if len(sys.argv) < 2:
		print("PLEASE PASS A FILE NAME... EXAMPLE: 'ingest.py test.csv'")
		exit(1)


def ingest_input():
	global 		plist
	global		flist
	plist     = []
	flist     = []

	with open(userfile) as opened:
		for line in opened:

			try:
				fields    = re.split(r'[ ,|"]+', line.replace('\n', ''))
				LastName  = fields[0]
				FirstName = fields[1]
				Gender    = fields[2]
				FavColor  = fields[3]
				DOB       = fields[4]
				plist.append({"lastname": LastName, "firstname": FirstName,  "dob": DOB, "favcolor": FavColor, "gender": Gender})

			except:
				flist.append(line.replace('\n', ''))

def print_output():
	print("ORDERED BY GENDER AND LAST NAME")
	print(json.dumps(sorted(plist, key=itemgetter('gender', 'lastname'))))


	print("ORDERED BY DOB")
	print(json.dumps(sorted(plist, key=itemgetter('dob'))))


	print("REVERSE ORDERED LAST NAME")
	print(json.dumps(sorted(plist, key=itemgetter('lastname'),reverse = True)))


	print("FAILED RECORDS")
	pprint(flist)



###################################################
#CALLS
###################################################
check_arguments()
ingest_input()
print_output()
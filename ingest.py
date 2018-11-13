#!/bin/python3
###################################################
#Guaranteed Rate Dev Homework
#Mike Thoma 11/11/2018
###################################################
#EXIT CODES
#1 UNSPECIFIED/GENERAL FAILURE
#2 NO ARGUMENT GIVEN
#3 ALL RECORD PROCESSING FAILED
#4 NO RECORDS DETECTED
###################################################
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
global 		  plist
global		  flist
userfile    = sys.argv[-1]
#people list
plist       = []
#failure list
flist       = []

###################################################
#FUNCTIONS
###################################################
def check_arguments():
	if len(sys.argv) < 2:
		print("PLEASE PASS A FILE NAME... EXAMPLE: 'ingest.py test.csv'")
		exit(2)


def ingest_input():
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

	#if only people list is populated...
	if plist:

		print("ORDERED BY GENDER AND LAST NAME")
		print(json.dumps(sorted(plist, key=itemgetter('gender', 'lastname'))))


		print("ORDERED BY DOB")
		print(json.dumps(sorted(plist, key=itemgetter('dob'))))


		print("REVERSE ORDERED LAST NAME")
		print(json.dumps(sorted(plist, key=itemgetter('lastname'),reverse = True)))

		#and print failures if we have any
		if flist:
			print("FAILED RECORDS")
			print(flist)
		#that's all folks
		exit(0)

	#otherwise if people list is empty and failure list is populated
	elif not plist and flist:
		print("ALL RECORDS FAILED")
		print(flist)
		exit(3)

	#otherwise if no people list and no failure list
	elif not flist and not plist:
		print("NO RECORDS DETECTED")
		exit(4)

	#otherwise something else failed
	else:
		print("SCRIPT FAILED UKNOWN ERROR...")
		exit(1)

###################################################
#CALLS
###################################################
check_arguments()
ingest_input()
print_output()
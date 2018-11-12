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
userfile  = sys.argv[-1]

###################################################
#FUNCTIONS
###################################################
def check_arguments():
	if len(sys.argv) < 2:
		print("PLEASE PASS A FILE NAME... EXAMPLE: 'ingest.py test.csv'")
		exit(1)


def ingest_input():
	global      people
	global      iteration
	global 		tlist
	iteration = 0
	people    = {}
	tlist     = []

	with open(userfile) as opened:
		for line in opened:

			iteration += 1
			fields    = re.split(r'[ ,|"]+', line)

			LastName  = fields[0]
			FirstName = fields[1]
			Gender    = fields[2]
			FavColor  = fields[3]
			DOB       = fields[4]
	
			# people[iteration] = {}
			# people[iteration]['lastname' ] = LastName
			# people[iteration]['firstname'] = FirstName
			# people[iteration]['gender'   ] = Gender
			# people[iteration]['favcolor' ] = FavColor
			# people[iteration]['dob'      ] = DOB

			tlist.append({"lastname": LastName, "firstname": FirstName,  "dob": DOB, "favcolor": FavColor, "gender": Gender})



###################################################
#CALLS
###################################################
check_arguments()
ingest_input()

print("ORDERED BY GENDER AND LAST NAME")
pprint(sorted(tlist, key=itemgetter('gender', 'lastname')))


print("ORDERED BY DOB")
pprint(sorted(tlist, key=itemgetter('dob')))


print("REVERSE ORDERED LAST NAME")
pprint(sorted(tlist, key=itemgetter('lastname'),reverse = True))
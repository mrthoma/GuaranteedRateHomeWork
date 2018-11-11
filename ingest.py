#!/bin/python3
###################################################
#Guaranteed Rate Dev Homework
#Mike Thoma 11/11/2018

###################################################
#REQUIREMENTS
###################################################
import sys
import re
import csv

###################################################
#VARIABLES
###################################################
userfile      = sys.argv[-1]

###################################################
#FUNCTIONS
###################################################
def check_arguments():
	if len(sys.argv) < 2:
		print("PLEASE PASS A FILE NAME... EXAMPLE: 'ingest.py test.csv'")
		exit(1)


def print_output():
	with open(userfile) as opened:
		for line in opened:
			fields    = re.split(r'[ ,|"]+', line)
			print(fields)
			LastName  = fields[0]
			FirstName = fields[1]
			Gender    = fields[2]
			DOB       = fields[3]
	
			print("Last Name Is "  + LastName )
			print("First Name Is " + FirstName)
			print("Gender Is "     + Gender   )  
			print("DOB Is "        + DOB      )


###################################################
#CALLS
###################################################
check_arguments()
print_output()
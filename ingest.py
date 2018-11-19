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
#REQUIREMENTS
###################################################
import     sys
import     json
from       processdata import process_input, get_order_dob, get_order_gender, get_order_reverse_lastname, get_recordcount, get_failcount, get_flist
userfile = sys.argv[-1]

#Functions
def check_arguments():
	#check if filename was passed
	if len(sys.argv) < 2:
		print("PLEASE PASS A FILE NAME... EXAMPLE: 'ingest.py test.csv'")
		exit(2)


def ingest_file():
	with open(userfile) as opened:
		for line in opened:
			#don't want to error on a line
			try:
				process_input(line)
			except:
			#failed records being recorded... so let's pass the ex
				pass

def print_output():

	recordcount = get_recordcount()
	failcount   = get_failcount()

	#if records successfully populated...
	if recordcount > 0:

		print("ORDERED BY GENDER AND LAST NAME:")
		print(json.dumps(get_order_gender()))


		print("ORDERED BY DOB:")
		print(json.dumps(get_order_dob()))


		print("REVERSE ORDERED LAST NAME:")
		print(json.dumps(get_order_reverse_lastname()))


		#and print failures if we have any
		if failcount > 0:
			print("FAILED RECORDS")
			print(get_flist())
		#that's all folks
		exit(0)

	#otherwise if recor list is empty and failure list is populated
	elif recordcount == 0 and failcount > 0:
		print("ALL RECORDS FAILED")
		print(get_flist())
		exit(3)

	#otherwise if no record list and no failure list
	elif recordcount == 0 and failcount == 0:
		print("NO RECORDS DETECTED")
		exit(4)

	#otherwise something else failed?
	else:
		print("SCRIPT FAILED UKNOWN ERROR...")
		exit(1)

#Calls
check_arguments()
ingest_file()
print_output()
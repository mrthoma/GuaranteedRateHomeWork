###################################################
Guaranteed Rate Dev Homework
Mike Thoma 11/11/2018
###################################################
REQUIREMENTS:

	pip3, python3, python flask, python flask_restful

ingest.py

	Description:
		Command line app to take in a filename as an argument and sort the records contained within.

	Usage:
		ingest.py <filename>

	File Expectations:
		File should contain records in the following format:

			LASTNAME|FIRSTNAME|GENDER(M/F)|FAVORITECOLOR|DOB(MM/DD/YYY)
				ex: "Thome|Michael|M|Red|09/22/1987"

		Each record should be on a new line.
		Accepted delimiters are: '| ,' (pipe, space and comma)
		File can contain multiple lines using any mix of delimiters

	Exit Codes:
	1 UNSPECIFIED/GENERAL FAILURE
	2 NO ARGUMENT GIVEN
	3 ALL RECORD PROCESSING FAILED
	4 NO RECORDS DETECTED


processdata.py

	Description:
		Module with functions for parsing and sorting the records for both the command line and REST portion
	Usage:
		No direct usage: module to be used with command line and REST portion of the file


rest_ingest.py and start.sh

	Requirements:
		python3, python flask, python flask_restful

	Description:
		REST program written in python FLASK framework to take in a single record via plain text POST, store that information while the program is running, and be able to sort the records that have been posted. There is no consistent data store for this REST API, so all records are lost when restarting.
	Usage:

		Use "start.sh" to start FLASK environment once requirements have been installed. You can run this via screen if you wish to keep it running and still do work.

		Post should contain record in the following format:
				LASTNAME|FIRSTNAME|GENDER(M/F)|FAVORITECOLOR|DOB(MM/DD/YYY)
				ex: "Thome|Michael|M|Red|09/22/1987"

		To POST a record:
			curl -X POST -H "Content-Type: text/plain" --data "LASTNAME|FIRSTNAME|GENDER(M/F)|FAVORITECOLOR|DOB(MM/DD/YYY)" 127.0.0.1:5000/records

		To GET records sorted by Gender and Last Name:
			curl 127.0.0.1/records/gender

		To GET records sorted by reverse LastName:
			curl 127.0.0.1/records/name 

		To GET records sorted by Birthdate:
			curl 127.0.0.1/records/birthdate
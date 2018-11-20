#!/bin/python3
###################################################
#Guaranteed Rate Dev Homework
#REST Portion
#Mike Thoma 11/11/2018
###################################################
#from ingest import print_output
import re
import json
from   flask         import Flask, request, jsonify, Response
from   flask_restful import Resource, Api
from   processdata   import process_input, get_order_dob, get_order_gender, get_order_reverse_lastname, get_flist
app = Flask(__name__)
api = Api(app)

###################################################
#VARIABLES
###################################################

#FUNCTIONS
class Records(Resource):
	def post(self):

		userpost = request.data.decode('utf-8')

		#check if request was empty
		if userpost == "":
			return("REQUEST WAS EMPTY.... EXPECTING: LASTNAME | FIRSTNAME | GENDER | FAVORITE COLOR | DOB")

		#check if request was in proper format
		elif not re.search(r'[ ,|]+', userpost):
			return("NOT USING PROPER DELIMITERS: | , ")
		#finally lets see if the fields are okay
		try:
			process_input(userpost)
		except:
			return("FAILED TO PROCESS RECORD... EXPECTING: LASTNAME | FIRSTNAME | GENDER | FAVORITE COLOR | MM/DD/YYYY")
		return("SUCCESS")


class OrderByGender(Resource):
	def get(self):
		return Response(json.dumps(get_order_gender(), indent=4))

class OrderByDOB(Resource):
	def get(self):
		return Response(json.dumps(get_order_dob(), indent=4))

class OrderByReverseLastName(Resource):
	def get(self):
		return Response(json.dumps(get_order_reverse_lastname(), indent=4))

###################################################
#ROUTES
###################################################
api.add_resource(Records, '/records')
api.add_resource(OrderByGender, '/records/gender')
api.add_resource(OrderByDOB, '/records/birthdate')
api.add_resource(OrderByReverseLastName, '/records/name')
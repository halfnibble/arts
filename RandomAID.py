#!/usr/bin/env python

import random

def AID_gen():
	aid_0 = ""
	aid_1 = ""
	
	# Create list of carrier prefixes for call signs...
	callsignsA = ("UAL", "AAL", "N", "USA", "NWA", "SWA", "VADER", "DOOM", "N")
	# List of suffixes for Genearl Avation..example: N344C (C)
	callsignsB = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","G","H","K","L","M","N","P","Q","R","S","T","W","V")
	
	# Generate random carrier prefix
	aid_0 = random.choice(callsignsA)
	
	# If General Aviation, append string of numbers and up to one letter
	if aid_0 == "N":
		aid_1 = str(random.randint(10,999)) + str(random.choice(callsignsB))
	# For military aircraft ad up to two digits to call sign
	elif (aid_0 == "VADER" or aid_0 == "DOOM"):
		aid_1 = random.randint(1,99)
	# Air Carriers (Taxis) will have two to three digits appended to call sign
	else:
		aid_1 = random.randint(10,899)
	
	#aid will be used as AID in practice system
	aid = aid_0 + str(aid_1)
	
	return aid
	



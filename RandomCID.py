#!/usr/bin/env python

import random

def CID_gen():
	
	# Create a cid from 1 - 200
	# Real ATC systems go beyong 999, but academy tends to NOT
	CID_value = random.randint(1,200)
	
	# Make the CID a string and append zeros to front if necessary
	# in order to make all CIDs three digits
	if(len(str(CID_value)) == 1):
		CID = str("00") + str(CID_value)
	elif(len(str(CID_value)) == 2):
		CID = str("0") + str(CID_value)
	else:
		CID = str(CID_value)
	
	return CID
	



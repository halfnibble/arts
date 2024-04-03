#!/usr/bin/env python

import random

# Create a random time in military format
def TME_gen():

	# Start by Generating an hour between 00 and 23
	Hour_value = random.randint(0,23)
	# This procedure will turn single digits into two digits
	# i.e. "8" wil become "08"
	if(Hour_value <= 9):
		Hour_value = str("0") + str(Hour_value)
	else:
		Hour_value = str(Hour_value)
		
	# Now generate minutes beween 00 and 59
	Min_value = random.randint(0,59)
	if(Min_value <= 9):
		Min_value = str("0") + str(Min_value)
	else:
		Min_value = str(Min_value)
		
	TIME = Hour_value + Min_value
	
	return TIME

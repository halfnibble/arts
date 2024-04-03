#!/usr/bin/env python

import random

def ALT_gen():
	
	# Genereate a random altitude between 060 and 230
	# Keep the integer property for numerical comparisons
	# i.e. 060 does equal 60 and vice versa for integers, but not strings
	ALT = random.randrange(60, 230, 10)
	
	# when Using Python for logic, make ALT an int: return ALT
	# for javascript logic, use the following:
	ALT = str(ALT)

	return ALT

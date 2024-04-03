#!/usr/bin/env python

import random

def BCN_gen():
	
	# Create four randomly generated integers, and concatenate
	# them as a numerical string
	
	# First digit can be one through six,
	# Not zero, because that would be silly, and
	# not seven because of possibility of generating EMRG,RDOF, etc.
	BCN_0 = random.randint(1,6)
	BCN_1 = random.randint(0,7)
	BCN_2 = random.randint(0,7)
	BCN_3 = random.randint(0,7)
	
	BCN = str(BCN_0) + str(BCN_1) + str(BCN_2) + str(BCN_3)
	
	return BCN
	


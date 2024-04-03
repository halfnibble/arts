#!/usr/bin/env python

import random

# Generate a suitable speed for aircraft type:
def SPD_gen(AID):
	
	# Randomly create slower speeds for General Aviation aircraft:
	# Make sure "N" is not from Northwest Airlines
	if "N" in AID and "NWA" not in AID:
		SPEED = random.randrange(100, 210, 10)
	# All other aircraft get faster speeds:
	else:
		SPEED = random.randrange(220, 480, 10)
	
	#make SPEED a string
	SPEED = str(SPEED)
		
	return SPEED

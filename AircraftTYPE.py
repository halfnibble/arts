#!/usr/bin/env python

import random

# Correlate Aircraft ID with a suitable Aircraft type
def Atype_gen(AID):
	
	# Create array of General Aviation types:
	GAtypes = ("BE9/A", "C172/T", "BE65/A", "C337/A", "C210/A", "PA27/A")
	# Create array of Air Carrier types:
	ACtypes = ("B722/A", "B747/I", "MD80/G", "B733/A", "DC9/A", "MD90/I", "B738/Q",  )
	# Create array of Military types:
	MILtypes = ("B52/Q", "C130/G", "T34/P", "F4/P", "V10/A", "4/F4/P")
	
	# Determine is aircraft is General Aviation:
	# Make sure "N" is not part of Norwest Airlines call sign
	if "N" in AID and "NWA" not in AID:
		TYPE = random.choice(GAtypes)
	# Detemine if aircraft is Military:
	elif ("DOOM" in AID or "VADER" in AID):
		TYPE = random.choice(MILtypes)	
	# All the rest are assumed to be Air Carriers:
	else:
		TYPE = random.choice(ACtypes)
		
	return TYPE


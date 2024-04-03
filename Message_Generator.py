#!/usr/bin/python

import RandomAID
import AircraftTYPE
import RandomCID
import RandomSPD
import RandomTME
import RandomBCN
import RandomALT
from XLS_parser import Message_Type, FIX, ROUTE, ENT_Route

AID = RandomAID.AID_gen()
TYPE = AircraftTYPE.Atype_gen(AID)
CID = RandomCID.CID_gen()
SPEED = RandomSPD.SPD_gen(AID)
TIME = RandomTME.TME_gen()
BCN = RandomBCN.BCN_gen()
ALT = RandomALT.ALT_gen()

class FlightPlan(object):

	@classmethod
	def FP_MSG(self):
		# This set of functions will determine whether or not the Flight Plan is
		# proposed or active. If active, it will give a Time_Statement that is 
		# "Estimating" the next fix. If proposed, it will give a "Proposed
		# departure" time statement. This function will also give appropriate 
		# altitude statements based on proposed or active flight status.
		if(FIX == ROUTE.split()[0]):
			#Proper Time Statement for proposed flights
			Time_Statement = "Proposed " + FIX + " departure at " + TIME + ". "
			# Proper Altitude Statement for proposed flights.
			Alt_Statement = "Requesting altitude of " + str(ALT) + ", "
	
		else:
			# Proper Time Statement for active flights:
			if(FIX == "HEZ" or FIX == "GLH"):
				Time_Statement = "Estimating the " + FIX + " VOR/DME at " + TIME + ". "
			else:
				Time_Statement = "Estimating the " + FIX + " VORTAC at " + TIME + ". "
			# Proper Altitude Statement for active flights:
			Alt_Statement = "Level at " + str(ALT) + ", "
		
		Problem = "Write down the flight plan onto a blank strip." \
		"Then enter the Flight Plan into the computer. <BR /><BR /> The following" \
		" aircraft: " + AID + ", a " + TYPE + \
		" is squawking code: " + BCN + ". Filed True Airspeed of " + \
		SPEED + "KTs. " + Time_Statement + Alt_Statement + "via " + ROUTE
		
		return Problem

	@classmethod	
	def FP_ANS(self):
		# Determine correct computer entry for time based on active vs.
		# inactive status.
		if(FIX == ROUTE.split()[0]):
			ENT_Time = "P" + TIME
		else:
			ENT_Time = "E" + TIME
		Answer = ['FP', AID, TYPE, BCN, SPEED, FIX, ENT_Time, ALT, ENT_Route]
		
		return Answer
		

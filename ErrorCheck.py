#!/usr/bin/env python

User_Answer = raw_input("")
User_Answer = User_Answer.split()
User_Answer[7] = int(User_Answer[7])

if(User_Answer == Answer):
	print "Accept"
else:
	print "Reject"
	print Answer
	print User_Answer

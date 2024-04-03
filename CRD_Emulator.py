#!/usr/bin/python

import Message_Generator
import Temp
import cgi
import cgitb
cgitb.enable()


form = cgi.FieldStorage()
if "Status" not in form:
	Status = "new"
else:
	Status = form['Status'].value
	Status = cgi.escape(Status)
	

if(Message_Generator.Message_Type == 'FP'):
	P = Message_Generator.FlightPlan()
	Problem = P.FP_MSG()
	Solution = P.FP_ANS()
	
elif(Message_Generator.Message_Type == 'AM'):
	print "we have-a no bananas"
	
else:
	print "no bananas today"

print 'Content-type: text/html\r'
print '\r'
print '<TITLE> Computer Messaging Practice</TITLE>'
Temp.Template(Problem, Solution, Status)


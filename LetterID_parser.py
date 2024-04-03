#!/usr/bin/env python

import csv
import random

# This will be used to create several dictionaries (one for each row in CSV)
dict_list = []
end_range = 0

# Creates a dictreader object name "r"
f = open("3LetterID.csv")
r = csv.DictReader(f,['IDENTIFIER', 'LOCATION', 'ID_NAME'])

for record in r:
	dict_list.append(record)
	end_range = end_range + 1

# Determine maximum range for random selection of problems	
# end_range = len(dict_list)
# This din't work for some reason...maybe I needed to subtract 1..oh well.

# Randomly select a problem for the D-CRD EMU to use:
selection = random.randint(0, (end_range-1))

# Now create the variables necessary to setup the problem:
IDENTIFIER = dict_list[selection]['IDENTIFIER']
LOCATION = dict_list[selection]['LOCATION']
ID_NAME = dict_list[selection]['ID_NAME']






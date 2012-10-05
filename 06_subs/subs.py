#!/usr/bin/python
"""Finds all occurences of substring string2 in string1 from a datafile of format "string1\\nstring2" """

import sys

usage = """subs.py [data file]
Find all occurances of a substring string2 ni string1 from a datafile of format: \nstring1\nstring2 """
data_file_loc = "test_data"
argc = len(sys.argv)

if(argc > 2):
	print(usage)
	sys.exit(1)
if(argc == 2):
	data_file_loc = sys.argv[1]
try:
	data_file = open(data_file_loc)
	superstring = data_file.readline()
	substring = data_file.readline()
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

if(superstring[-1] == '\n'):
	superstring = superstring[:-1]
if(substring[-1] == '\n'):
	substring = substring[:-1]

if(len(superstring) < len(substring)):
	print("substring is longer than superstring! Malformed data file")

index = 0
final_index = len(superstring)
subindex = 0
final_subindex = len(substring)
substring_locations = []
broken = False

while(index < final_index):
	if(superstring[index] == substring[0]):
		if(final_subindex == 1):
			substring_locations.append(index + 1)
		elif(index + final_subindex > final_index):
			break
		else:
			while((subindex < final_subindex) and 
			      (subindex + index < final_index)):
				if(superstring[index + subindex] ==
				   substring[subindex]):
					subindex += 1
				else:
					broken = True
					break
			if not broken:
				#why u no read indexes right rosalind
				substring_locations.append(index + 1)
			else:
				broken = False
			subindex = 0
	index += 1

for entry in substring_locations:
	print("%s" % entry),

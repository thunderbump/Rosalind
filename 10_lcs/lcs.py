#!/usr/bin/python
"""Finds the longest common substring among all genetic sequences in a data file"""

import sys

usage = """lcs.py [data file]
Finds the longest common substring among all genetic sequences in data file"""
argc = len(sys.argv)
data_file_loc = "test_data"

if argc > 2:
	print(usage)
	sys.exit(1)
if argc == 2:
	data_file_loc = sys.argv[1]

sequences = []

try:
	data_file = open(data_file_loc)
	for line in data_file:
		if line[-1] == '\n':
			line = line[:-1]
		sequences.append(line)
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

def is_substring(super_str, sub_str):
	index = 0
	final_index = len(super_str)
	subindex = 0
	final_subindex = len(sub_str)
	substring_found = False
	broken = False

	while(index < final_index):
		if(super_str[index] == sub_str[0]):
			if(final_subindex == 1):
				substring_locations.append(index + 1)
			elif(index + final_subindex > final_index):
				break
			else:
				while((subindex < final_subindex) and 
				      (subindex + index < final_index)):
					if(super_str[index + subindex] ==
					   sub_str[subindex]):
						subindex += 1
					else:
						broken = True
						break
				if not broken:
					substring_found = True
				else:
					broken = False
				subindex = 0
		index += 1
	return substring_found

def find_substrings(super_str, sub_str):
	pass

print 'asdf' in 'das'


#finding_substring = False
#substrings = sequences[0]
#sequence_index = 0
#max_sequence_index = len(sequences)
#while sequence_index < max_sequence_index:
#	index_break = False
#	str_index = 0
#	max_str_index = len(sequences[sequence_index])
#	substr_index = 1
#	while str_index < max_str_index - 1:
#		if(is_substring(sequence[sequence_index], 
#	sequence_index += 1

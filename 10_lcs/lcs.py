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

def find_substrings(super_str, sub_str):
	substrings = ['']
	for str_index in range(0,len(sub_str) + 1):
		current_sub_str = ''
		for index in range(str_index,len(sub_str) + 1):
			if(sub_str[str_index:index] in super_str):
				current_sub_str = sub_str[str_index:index]
		if(current_sub_str != [] and current_sub_str not in 
							substrings[-1]):
			substrings.append(current_sub_str)
	substrings.remove(substrings[0])
	return substrings
		
sub_string_list = [sequences[0]]
for sequence_index in range(1, len(sequences)):
	tmp_new_sub_string = []
	for substring in sub_string_list:
		new_sub_strings = find_substrings(sequences[sequence_index],
						  substring)
		for new_sub_string in new_sub_strings:
			tmp_new_sub_string.append(new_sub_string)
	sub_string_list = tmp_new_sub_string
biggest_sub_str = ''
for substr in sub_string_list:
	if len(substr) > len(biggest_sub_str):
		biggest_sub_str = substr
print biggest_sub_str 

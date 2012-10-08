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

substring = False

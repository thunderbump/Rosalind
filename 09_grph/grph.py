#!/usr/bin/python
"""Finds any adjacencies of order 3 in digraphs given by a data file in FASTA format"""

import sys

usage = """grph.py [data file]
Finds any adjacencies of order 3 in digraphs given by a data file in FASTA format"""
argc = len(sys.argv)
data_file_loc = "test_data"

if argc > 2:
	print(usage)
	sys.exit(1)
if argc == 2:
	data_file_loc = sys.argv[1]

labels = []
sequences = []
sequence_index = 0
try:
	data_file = open(data_file_loc)
	for line in data_file:
		if(line[-1] == '\n'):
			line = line[:-1]
		if(line[0] == '>'):
			labels.append(line[1:])
			sequences.append("")
			sequence_index += 1
		else:
			sequences[-1] = ''.join([sequences[-1], line])
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

overlaps = []
for primary_index, sequence in enumerate(sequences):
	for secondary_index, secondary_sequence in enumerate(sequences):
		if primary_index == secondary_index:
			continue
		if sequence[-3:] == secondary_sequence[:3]:
			overlaps.append([labels[primary_index],
					 labels[secondary_index]])
for overlap in overlaps:
	print(" ".join(overlap))

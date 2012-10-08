#!/usr/bin/python
"""Computes the GC content of a series of genetic sequences and returns the string with the highest GC content."""

import sys

usage = """gc.py [data file]
Computes the GC content of a series of genetic sequences and returns the stri
ng with the highest GC content. If a data file isn't given, "test_data" is used"""
argc = len(sys.argv)

at = "AT"
gc = "GC"
gc_totals = []
lengths = []
labels = []
sequences = []
data_file_loc = "test_data"

if(argc > 2):
	print(usage)
	sys.exit(1)
if(argc == 2):
	data_file_loc = sys.argv[1]

try:
	data_file = open(data_file_loc)
	sequence_counter = -1
	for line in data_file:
		if(line[-1] == '\n'):
			line = line[:-1]
		if(line[0] == '>'):
			sequence_counter += 1
			labels.append(line[1:])
			sequences.append("")
			lengths.append(0)
		else:
			sequences[sequence_counter] = ''.join([sequences[
							     sequence_counter],
							     line])
			lengths[sequence_counter] += len(line)
	data_file.close()
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

for counter, sequence in enumerate(sequences):
	current_gc = 0
	for gene in sequence:
		if gene in gc:
			current_gc += 1
	gc_totals.append(current_gc / float(lengths[counter]))
highest_gc = max(gc_totals)
highest_label = labels[gc_totals.index(highest_gc)]
print highest_label
print "%.2f%%" % (highest_gc * 100)


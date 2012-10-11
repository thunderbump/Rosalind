#!/usr/bin/python
"""Computes probability for a given gene in a sequence, the next gene in that sequence will be the same, given a GC index"""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """prob.py [data file]
Independantly computes probability for a given gene in a sequence, the next gene in that sequence will be the same, given a series of GC indexes."""

if argc > 2:
	print(usage)
	sys.exit(1)
if argc == 2:
	data_file_loc = sys.argv[1]

gc_content = []

try:
	data_file = open(data_file_loc)
	for line in data_file:
		if line[-1] == "\n":
			line = line[:-1]
		for prob in line.split(' '):
			gc_content.append(float(prob))
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

for prob in gc_content:
	pc = pg = prob / 2
	pa = pt = (1 - prob) / 2
	print("%1.3f" % (pa * pa + pc * pc + pg * pg + pt * pt)),

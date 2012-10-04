#!/usr/bin/python
"""Determine the hamming distance between two DNA sequences of equal length"""

import sys

argc = len(sys.argv)
test = True
test_file_loc = "test_data"
usage = """hamm.py [data file]
Compute the hamming distance between two DNA sequences. Both sequences must be
of equal length."""

if(argc > 2):
	print(usage)
	sys.exit(0)
elif(argc == 2):
	test = False
	test_file_loc = sys.argv[1]

try:
	test_file = open(test_file_loc)
	reference = test_file.readline()
	comparison = test_file.readline()
	test_file.close()
	if(reference[-1] == '\n'):
		reference = reference[:-1]
	if(comparison[-1] == '\n'):
		comparison = comparison[:-1]
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

if(len(reference) != len(comparison)):
	print("Pairs of data must be of equal length")

hamming_distance = 0
index = 0
max_index = len(reference)

while(index < max_index):
	if(reference[index] != comparison[index]):
		hamming_distance += 1
	index += 1
if(test):
	print("Ref  : %s" % reference)
	print("Test : %s" % comparison)
	print("Hamming distance : %d" % hamming_distance)
else:
	print(hamming_distance)
sys.exit(0)

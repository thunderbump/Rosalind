#!/usr/bin/python
"""Computes the reverse compliment of a DNA sequence"""

import sys
import string

argc = len(sys.argv)
toCompliment = string.maketrans("ACGT", "TGCA")
test = True
test_file_loc = "test_data"
usage = """revc.py [data file]
Computes the reverse compliment of the given DNA sequence in 'data file'"""

if(argc > 2):
	print(usage)
	sys.exit(1)
elif(argc == 2):
	test_file_loc = sys.argv[1]
	test = False

try:
	test_file = open(test_file_loc)
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

data = test_file.readline()
if(data[-1] == '\n'):
	data = data[:-1]
test_file.close()
if(test):
	print("orig data: %s" % data)
answer = data[::-1].translate(toCompliment)
if(test):
	print("revc data: %s" % answer)
else:
	print(answer)

sys.exit(0)

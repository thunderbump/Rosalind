#!/usr/bin/python
"""Transcribes T to U simulating RNA transcription on a given DNA sequence
I'm avoiding the obvious `tr "T" "U" < test_data`"""

import sys
import string

argc = len(sys.argv)
test = True
test_file_loc = "test_data"
toRNA = string.maketrans('T', 'U')
usage = """rna.py [data file]
Simulates RNA transcription on a DNA sequence given in 'data file'"""

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

test_data = test_file.readline()
test_file.close()

if(test):
	print("DNA: %s" % test_data),
test_answer = test_data.translate(toRNA)
if(test):
	print("RNA: %s" % test_answer),
else:
	print(test_answer),

#!/usr/bin/python
"""Solution for http://rosalind.info/problems/dna/
Assuming:
1) single line of data
2) data only contains 'A', 'C', 'G', and 'T'. Other characters will be ignored
"""
import sys
###############
# Global Vars #
###############

test_data_file = "test_data"
test = True
usage = """dna.py [data file]
Count nucleotides found in first line of "data file". if no file provided,
the script uses test_data"""

########
# Main #
########

if(len(sys.argv) > 2):
	print(usage)
	sys.exit(1)
elif(len(sys.argv) == 2):
	test = False
#	try
	data_file_object = open(sys.argv[1])
#	except
else:
	data_file_object = open(test_data_file)

data = data_file_object.readline()
totals = {'A':0, 'C':0, 'G':0, 'T':0}
for char in data:
	if char in totals.keys():
		totals[char] += 1
if test:
	print(" A  C  G  T")
print("%d %d %d %d" % (totals['A'], totals['C'], totals['G'], totals['T']))

sys.exit(0)

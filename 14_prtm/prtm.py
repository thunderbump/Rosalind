#!/usr/bin/python

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
weight_table = {'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 
                'F':147.06841, 'G':57.02146, 'H':137.05891, 'I':113.08406, 
                'K':128.09496, 'L':113.08406, 'M':131.04049, 'N':114.04293, 
                'P':97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203, 
                'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333}
usage = """prtm.py [data file]
Compute the weights of the codon sequences found in data file"""

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

weights = []
for sequence in sequences:
    weights.append(0)
    for codon in sequence:
        weights[-1] += weight_table[codon]

for weight in weights:
    print("%.2f" % weight)

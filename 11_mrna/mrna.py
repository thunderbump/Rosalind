#!/usr/bin/python
"""Computes how many possable rna transcriptions could have been the source of codon sequences found in the data file."""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """mrna.py [data file]
Computes how many possable rna transcriptions could have been the source of codon sequences found in the data file."""
codon_total = {'F':2, 'L':6, 'S':6, 'Y':2, 'C':2, 'W':1, 'P':4, 'H':2, 'Q':2,
	       'R':6, 'I':3, 'M':1, 'T':4, 'N':2, 'K':2, 'V':4, 'A':4, 'D':2,
               'E':2, 'G':4, 'STOP':3}

if argc > 2:
	print(usage)
	sys.exit(1)
if argc == 2:
	data_file_loc = sys.argv[1]

codon_sequences = []
try:
	data_file = open(data_file_loc)
	for line in data_file:
		if line[-1] == '\n':
			line = line[:-1]
		codon_sequences.append(line)
	data_file.close()
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

possible_gene_sequences = []
for sequence in codon_sequences:
	possible_gene_sequences.append(1)
	for codon in sequence:
		possible_gene_sequences[-1] *= codon_total[codon]
	possible_gene_sequences[-1] *= codon_total['STOP']
for nck in possible_gene_sequences:
	print nck

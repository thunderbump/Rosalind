#!/usr/bin/python
"""Find the likely common ancestor from a set of genetic sequences"""

import sys

argc = len(sys.argv)
usage = """subs.py [data file]
Find the likely common ancestor from a set of genetic sequences"""
data_file_loc = "test_data"
gene_sequences = []
totals = [[], [], [], []]
genes = "ACGT"
index_translation = {'A':0, 'C':1, 'G':2, 'T':3}

if(argc > 2):
	print(usage)
	sys.exit(1)
if(argc == 2):
	data_file_loc = sys.argv[1]

try:
	data_file = open(data_file_loc)
	for line in data_file:
		gene_sequences.append(line)
	data_file.close()
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

index = 0
max_gene = len(gene_sequences)
while(index < max_gene):
	if(gene_sequences[index][-1] == '\n'):
		gene_sequences[index] = gene_sequences[index][:-1]
	index += 1

normal = len(gene_sequences[0])
for sequence in gene_sequences:
	if(len(sequence) != normal):
		print("gene sequences must be the same length")

sequence_index = 0
gene_index = 0
max_sequence = len(gene_sequences[0])

while(sequence_index < max_sequence):
	for sequence in totals:
		sequence.append(0)
	while(gene_index < max_gene):
		totals[index_translation[
			gene_sequences[gene_index][sequence_index]]][
			sequence_index] += 1
		gene_index += 1
	gene_index = 0
	sequence_index += 1

sequence_index = 0
gene_index = 0
max_gene_label = []
max_gene_value = []
while(sequence_index < max_sequence):
	max_gene_label.append(0)
	max_gene_value.append(0)
	while(gene_index < 4):
		if(totals[gene_index][sequence_index] > 
		   max_gene_value[sequence_index]):
			
			max_gene_value[sequence_index] = totals[gene_index][
							        sequence_index]
			max_gene_label[sequence_index] = genes[gene_index]
		gene_index += 1
	gene_index = 0
	sequence_index += 1
		

likely_ancestor = ''.join(max_gene_label)
print(likely_ancestor)
sequence_index = 0
gene_index = 0
while(gene_index < 4):
	print("%s:" % genes[gene_index]),
	print(' '.join("%s" % total for total in totals[gene_index]))
	gene_index += 1



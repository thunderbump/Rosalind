#!/usr/bin/python
"""Finds all reading frames given by the dna sequences in data file"""

import sys
import string

argc = len(sys.argv)
data_file_loc = "test_data"
#just ignored U in this. one less step for translating since they're just
#going to be abstracted anyway
acid_weights = {'T':0, 'C':1, 'A':2, 'G':3}
weight_translation = 'FFLLSSSSYY\n\nCC\nWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
toCompliment = string.maketrans("ACGT", "TGCA")
usage = """orf.py [data file]
Finds all reading frames given by the dna sequences in data file"""

#copy-pasta from 05_prot
def acid_translate(acid_string):
	if(acid_string[-1] == '\n'):
		acid_string = acid_string[:-1]
	#if(len(acid_string) % 3 != 0):
	#	print("acids must be in groups of 3(len % 3 = 0)")
	#	sys.exit(1)
	translated_string = ""
	current_char_weight = 0
	current_char_progress = 2
	for char in acid_string:
		current_char_weight += acid_weights[char] * (
					4 ** current_char_progress)
		current_char_progress -= 1
		if(current_char_progress == -1):
			current_char_progress = 2
			translated_string += weight_translation[
						current_char_weight]
			current_char_weight = 0
	return translated_string

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
		#sequences.append(line.translate(toCompliment))
		#sequences.append(line[::-1])
		sequences.append(line[::-1].translate(toCompliment))
except IOError, error:
	print(error)
	print(usage)
	sys.exit(1)

tr_seq = []
end_tr_seq = []
for sequence in sequences:
	tr_seq.append(acid_translate(sequence))
	for displacement in range(1,3):
		end_displacement = (3 - displacement) % 3
		sequence[displacement:-end_displacement]
		tr_seq.append(acid_translate(sequence[displacement:
							-end_displacement]))
for sequence in tr_seq:
	start_indices = []
	end_indices = []
	for index, char in enumerate(sequence):
		if char == 'M':
			start_indices.append(index)
		if char == '\n':
			end_indices.append(index)
	for index in start_indices:
		for subindex in end_indices:
			if subindex > index:
				if sequence[index:subindex] not in end_tr_seq:
					end_tr_seq.append(sequence[index:
								subindex])
				break
for sequence in  end_tr_seq:
	 print(sequence)


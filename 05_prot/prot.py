#!/usr/bin/python
"""Translates a genetic sequence to a 'genetic string' made up of
genetic codons"""

import sys

argc = len(sys.argv)
acid_weights = {'U':0, 'C':1, 'A':2, 'G':3}
weight_translation = 'FFLLSSSSYY\n\nCC\nWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
usage = """prot.py [data file]
Translates an RNA sequence from acids to codons. If no data file is given,
prot.py reads the sequence from stdin(terminated by \\n)"""

def acid_translate(acid_string):
	if(acid_string[-1] == '\n'):
		acid_string = acid_string[:-1]
	if(len(acid_string) % 3 != 0):
		print("acids must be in groups of 3(len % 3 = 0)")
		sys.exit(1)
	translated_string = ""
	current_char_weight = 0
	current_char_progress = 3
	for char in acid_string:
		current_char_weight += (acid_weights[char] * 4 *
				        current_char_progress)
		current_char_progress -= 1
		if(current_char_progress == 1):
			translated_string += weight_translation[
						current_char_weight]
			current_char_progress = 3
			current_char_weight = 0
	return translated_string

if(argc > 2):
	print(usage)
elif(argc == 2):
	try:
		data_file = open(sys.argv[1])
		data = data_file.readline()
		data_file.close()
	except IOError, error:
		pass
else:
	data = raw_input()
print(acid_translate(data))

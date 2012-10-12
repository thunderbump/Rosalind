#!/usr/bin/python

import sys
import string

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """splc.py [data file]
Computes the final RNA strand from a mRNA strand in the first line of data file and given introns in subsequent lines"""
acid_weights = {'T':0, 'U':0, 'C':1, 'A':2, 'G':3}
weight_translation = 'FFLLSSSSYY\n\nCC\nWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'

def acid_translate(acid_string):
    if(acid_string[-1] == '\n'):
        acid_string = acid_string[:-1]
    if(len(acid_string) % 3 != 0):
        print("acids must be in groups of 3(len % 3 = 0)")
        sys.exit(1)
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

try:
    data_file = open(data_file_loc)
    mRNA = data_file.readline()
    if mRNA[-1] == '\n':
        mRNA = mRNA[:-1]
    introns = []
    for line in data_file:
        if line[-1] == '\n':
            line = line[:-1]
        introns.append(line)
except IOError, error:
    print(error)
    print(usage)
    sys.exit(1)
for intron in introns:
    mRNA = mRNA.replace(intron, '')

print acid_translate(mRNA),

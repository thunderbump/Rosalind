#!/usr/bin/python
"""Finds single substitution sequencing errors and offers corrections for
them.
Note this can be easily extended to the closest string if instead of just
searching for hamm == 1, look for the lowest hamming distance"""

import sys
import string

argc = len(sys.argv)
data_file_loc = "test_data"
toCompliment = string.maketrans("ACGT", "TGCA")
usage = """corr.py [data file]
Finds single substitution sequencing errors and offers corrections for
them. If no data file given, "test_data" is assumed."""

def revc(sequence):
    return sequence[::-1].translate(toCompliment)

def hamm(reference, comparison):
    hamming_distance = 0
    index = 0
    max_index = len(reference)

    while(index < max_index):
        if(reference[index] != comparison[index]):
            hamming_distance += 1
        index += 1
    return hamming_distance

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]

    try:
        data_file = open(data_file_loc)
        data = []
        for line in data_file:
            data.append(line.strip())
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)

    repeated = []
    non_repeated = []
    #compliment = []
    #find compliments
    #for string in data:
    #    compliment.append(revc(string))

    idx = 0
    #print len(data), "---"
    while idx < len(data):
    #    print idx
        if data[idx] in data[idx + 1:] or revc(data[idx]) in data: #or (
           #revc(data[idx])[::-1] in data or data[idx][::-1] in data):
            repeated.append(data[idx])
            #compliment = [sequence for sequence in compliment 
            #              if sequence != data[idx] and 
            #              sequence != revc(data[idx])]
            data = [sequence for sequence in data if sequence != data[idx] and
                    sequence != revc(data[idx])]
    #        print len(data), "--"
        else:
            non_repeated.append(data[idx])
            idx += 1
    #print len(data), len(non_repeated), "!---"
    #for string in data:
    #    if (string not in data[data.index(string) + 1:]
    #       ) and string not in compliment:
    #        non_repeated.append(string)
    for string in non_repeated:
        broken = False
        for candidate in repeated:
            #print revc(candidate), hamm(string, revc(candidate))
            #print string
            #print candidate, hamm(string, candidate)
            #raw_input()
            if string == candidate:
                continue
            if hamm(string, candidate) == 1:
                #print string
                #print candidate
                print(string + '->' + candidate)
                #data = [seq for seq in data if seq != candidate]
                #broken = True
                broken = True
                break
            if hamm(string, revc(candidate)) == 1:
                print(string + '->' + revc(candidate))
                #data = [seq for seq in data if seq != candidate]
                broken = True
                break
        if not broken:
            print string, "pair not found"
        
        #if not broken:
        #    for candidate in compliment:
        #        if hamm(string, candidate) == 1:
        #            print("".join([string, "->", candidate]))
                    #print(string)
                    #print(candidate)
        #            break
            

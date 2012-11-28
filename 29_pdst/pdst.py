#!/usr/bin/python

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """pdst.py [data_file]"""

def hamm(reference, comparison):
    #if(len(reference) != len(comparison)):
    #    print("Pairs of data must be of equal length")

    hamming_distance = abs(len(reference) - len(comparison))
    index = 0
    max_index = min([len(reference), len(comparison)])

    while(index < max_index):
        if(reference[index] != comparison[index]):
            hamming_distance += 1
        index += 1
    return hamming_distance

def hamm_matrix(sequence_list):
    return_matrix = []
    for seq in sequence_list:
        line = []
        for other_seq in sequence_list:
            line.append(float(hamm(seq, other_seq))
                        / min([len(seq), len(other_seq)]))
        return_matrix.append(line)
    for thing in return_matrix:
        for other_thing in  thing:
            print("%1.2f" % other_thing),
        print

if __name__ == "__main__":
    if(argc > 2):
        print(usage)
        sys.exit(1)
    if(argc == 2):
        data_file_loc = sys.argv[1]
    
    sequences = []
    labels = []
    lengths = []
    try:
        data_file = open(data_file_loc)
        sequence_counter = -1
        for line in data_file:
            if(line[-1] == '\n'):
                line = line[:-1]
            if(line[0] == '>'):
                sequence_counter += 1
                labels.append(line[1:])
                sequences.append("")
                lengths.append(0)
            else:
                sequences[sequence_counter] = ''.join([sequences[
                                     sequence_counter],
                                     line])
                lengths[sequence_counter] += len(line)
        data_file.close()
    except IOError, error:
        print(error)
        print(usage)
        sys.exit(1)

    hamm_matrix(sequences)

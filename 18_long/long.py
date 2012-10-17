#!/usr/bin/python
"""Computes the shortest superstring of a series of substrings in a given datafile"""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """long.py [data file]
Computes the shortest superstring of a series of substrings in a given datafile"""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    data_file_loc = sys.argv[1]

try:
    data_file = open(data_file_loc)
    sub_seqs = []
    for line in data_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        sub_seqs.append(line)
    data_file.close()
except IOError, error:
    print(error)
    print(usage)
    sys.exit(1)

def check_collision(seqA, seqB):
    if seqA in seqB:
        return seqB
    if seqB in seqA:
        return seqA
    index = min(len(seqA), len(seqB))
    while index > 0:
        if seqA[:index] == seqB[len(seqB) - index:]:
            return "%s%s" % (seqB[:len(seqB) - index], seqA)
        if seqB[:index] == seqA[len(seqA) - index:]:
            return "%s%s" % (seqA[:len(seqA) - index], seqB)
        index -= 1

def find_collision(sequences):
    primary = sequences.pop(0)
    min_len_diff = sys.maxint
    min_len_index = None
    min_len_seq = None
    for index, sequence in enumerate(sequences):
        candidate = check_collision(primary, sequence)
        if candidate == None:
            continue
        vanilla_len = max(len(sequence), len(primary))
        post_len = len(candidate)
        if min_len_diff > (post_len - vanilla_len):
            min_len_diff = (post_len - vanilla_len)
            min_len_index = index
            min_len_seq = candidate
    if min_len_seq == None:
        min_len_sequence = primary
        sequences.append("")
        min_len_index = -1
    sequences.pop(min_len_index)
    sequences.append(min_len_seq)
    return sequences

while len(sub_seqs) > 1:
    sub_seqs = find_collision(sub_seqs)
print sub_seqs[0]

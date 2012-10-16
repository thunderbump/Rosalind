#!/usr/bin/python

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
#def find_collision(sequences):
#    primary = sequences.pop(0)
#    print "primary", primary
#    candidates = []
#    candidate_parent = []
#    print sequences
#    for sequence in sequences:
#        candidates.append(check_collision(primary, sequence))
#        candidate_parent.append(sequence)
#    print "candidates:", candidates
#    longest_candidate_length = 0
#    longest_candidate_parent = None
#    longest_candidate = None
#    for cand_index, candidate in enumerate(candidates):
#        print candidate
#        if candidate == None:
#            continue
#        if len(candidate) > longest_candidate:
#            longest_candidate_length = len(candidate)
#            longest_candidate_parent = candidate_parent[cand_index]
#            longest_candidate = candidate
#    print sequences, len(sequences)
#    #if longest_candidate_parent:
#    print longest_candidate_parent
#    sequences.remove(longest_candidate_parent)
#    sequences.append(longest_candidate)
#    
#    return sequences

while len(sub_seqs) > 1:
    if None in sub_seqs:
        sub_seqs.remove(None)
    print sub_seqs
    sub_seqs = find_collision(sub_seqs)
    print(len(sub_seqs))
print sub_seqs

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
        if line[-1] == '\r':
            line = line[:-1]
        sub_seqs.append(line)
    data_file.close()
except IOError, error:
    print(error)
    print(usage)
    sys.exit(1)

def check_collision(seqA, seqB):
#    print seqA, "\n", len(seqA)
#    print seqB, "\n", len(seqB)
#    print seqA[:516]
#    print seqB[999-516:]
#    for char in seqB[999-516:]:
#        print "%r %s" % (char, char)
#    for index, char in enumerate(seqB[999-516:]):
#        print char, seqA[index]
#        if seqA[index] != char:
#            print index, seqA[index], '-', char
#    print seqA[:516] == seqB[999-516:]
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
#    print "collision not found" , seqA,"\n", seqB

def find_collision(sequences):
    primary = sequences.pop(0)
    min_len_diff = sys.maxint
    min_len_index = None
    min_len_seq = None
#    if None in sequences:
#        sequences.remove(None)
    for index, sequence in enumerate(sequences):
#        print index
        candidate = check_collision(primary, sequence)
        if candidate == None:
#            print "--", index
            continue
        vanilla_len = max(len(sequence), len(primary))
        post_len = len(candidate)
        if min_len_diff > (post_len - vanilla_len):
#            print "#", index
            min_len_diff = (post_len - vanilla_len)
            min_len_index = index
            min_len_seq = candidate
    if min_len_seq == None:
#        print "No collision found for %s" % primary[:20]
        min_len_sequence = primary
        sequences.append("")
        min_len_index = -1
    sequences.pop(min_len_index)
    sequences.append(min_len_seq)
    return sequences

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

#for seq in sub_seqs:
#print check_collision(sub_seqs[0], sub_seqs[7])

while len(sub_seqs) > 1:
#    print len(sub_seqs)
    sub_seqs = find_collision(sub_seqs)
print sub_seqs[0]

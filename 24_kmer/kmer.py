#!/usr/bin/python
"""Finds the number of occurences of all k-mers(for a given k sorted 
lexographically) in a given sequence given in FASTA format."""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """kmer.py k [data file]
Finds the number of occurences of all k-mers(for a given k sorted
lexographically) in a given sequence given in FASTA format. If no data
file is given, test_data is used"""

if __name__ == "__main__":
    if argc not in (2, 3):
        print(usage)
        sys.exit(1)
    if argc == 3:
        data_file_loc = sys.argv[2]
    try:
        K = int(sys.argv[1])
    except ValueError:
        print(usage)
        print("K must be numeric")
        sys.exit(1)

    try:
        data_file = open(data_file_loc)
        label = ""
        data = ""
        for line in data_file:
            if line[-1] == '\n':
                line = line[:-1]
            if line[-1] == '\r':
                line = line[:-1]
            if line[0] == '>':
                label = line
            else:
                data = "".join([data, line])
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)

    kmers = {}
    alphabet = "ACGT"
    all_kmers = ['']
    for index in range(0, K):
        scratch = []
        for string in all_kmers:
            for letter in alphabet:
                scratch.append(''.join([string, letter]))
        all_kmers = scratch
    for kmer in all_kmers:
        kmers[kmer] = 0
    index = 0
    while index <= len(data) - K:
        kmers[data[index:index + K]] += 1
        index += 1
    for key in sorted(kmers.keys()):
        print kmers[key],

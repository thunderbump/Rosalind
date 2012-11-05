#!/usr/bin/python
"""Finds the longest subsequence between two other genetic sequences"""

import sys
import string
import smith_waterman

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """lcsq.py [data file]
Finds the longest subsequence between two other genetic sequences given in
data file"""

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]

    try:
        data_file = open(data_file_loc)
        seq1 = data_file.readline().strip()
        seq2 = data_file.readline().strip()
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)

    (cor_seq1, cor_seq2) = smith_waterman.sequence_comparison(seq1, seq2)
    (cor_seq2x, cor_seq1x) = smith_waterman.sequence_comparison(seq2, seq1)
    substring = ""
    substringx = ""
    for index in range(len(cor_seq1)):
        if(cor_seq1[index] == cor_seq2[index]):
            substring = "%s%s" % (substring, cor_seq1[index])
    for index in range(len(cor_seq1x)):
        if(cor_seq1x[index] == cor_seq2x[index]):
            substringx = "%s%s" % (substring, cor_seq1x[index])
    if len(substring) > len(substringx):
        print substring
    else:
        print substringx

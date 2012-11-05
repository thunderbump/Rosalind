#!/usr/bin/python
"""Computes common genetic sequences via a smith-waterman scoring matrix."""

import sys
import string

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """smith_waterman.py [data file]
Computes common genetic sequences via a smith-waterman scoring matrix. Only
call directly for testing."""

def build_matrix(seq1, seq2):
    """Builds a smith_waterman matrix from seq1 and seq2"""
    matrix = list(list(0 for entry in range(len(seq2))) for other_entry
                  in range(len(seq1)))
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if seq1[i] == seq2[j]:
                dij = 2
            else:
                dij = -1
            matrix[i][j] = max(0, matrix[i-1][j-1] + dij,
                               matrix[i-1][j] - 1,
                               matrix[i][j-1] - 1)
    return matrix

def sequence_comparison(seq1, seq2):
    """Uses build matrix to find the collision between seq1 and seq2"""
    matrix = build_matrix(seq1, seq2)
    max_j = matrix[-1].index(max(matrix[-1]))
    bottom_row = [matrix[i][-1] for i in range(len(matrix))]
    max_i = bottom_row.index(max(bottom_row))
    if matrix[-1][max_j] > bottom_row[max_i]:
        max_i = len(matrix) - 1
    else:
        max_j = len(matrix[-1]) - 1
    i = max_i
    j = max_j
    seq1_corrected = ''
    seq2_corrected = ''
    while matrix[i][j] != 0:
        choices = [matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]]
        if max(choices) == choices[0]:
            seq1_corrected = "%s%s" % (seq1[i], seq1_corrected)
            seq2_corrected = "%s%s" % (seq2[j], seq2_corrected)
            i = i-1
            j = j-1
        elif max(choices) == choices[1]:
            seq1_corrected = "-%s" % seq1_corrected
            seq2_corrected = "%s%s" % (seq2[j-1], seq2_corrected)
            j = j-1
        else:
            seq1_corrected = "%s%s" % (seq1[i-1], seq1_corrected)
            seq2_corrected = "-%s" % seq2_corrected
            i = i-1
    return (seq1_corrected, seq2_corrected)


if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]
    try:
        data = []
        data_file = open(data_file_loc)
        for line in data_file:
            data.append("-%s" % line.strip())
        print data
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)

    sequence_comparison(data[0], data[1])
    sequence_comparison(data[2], data[3])
    sequence_comparison(data[0], data[2])
    sequence_comparison(data[0], data[3])

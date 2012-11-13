#!/usr/bin/python
"""Computes common genetic sequences via a smith-waterman scoring matrix."""

import sys
import string
from array import array

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """smith_waterman.py [data file]
Computes common genetic sequences via a smith-waterman scoring matrix. Only
call directly for testing."""

def build_matrix(seq1, seq2):
    """Builds a smith_waterman matrix from seq1 and seq2"""
    matrix = list(list(0 for entry in range(len(seq2))) for other_entry
                  in range(len(seq1)))
    #array implimentation 2-3x slower, blist implementation doesn't finish
    #5 minutes.
    #matrix = list(array('L', (0 for entry in range(len(seq2)))) for other_entry
    #              in range(len(seq1)))
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if seq1[i] == seq2[j]:
                dij = 5
            else:
                dij = -3
            matrix[i][j] = max(0, matrix[i-1][j-1] + dij,
                               matrix[i-1][j] - 3,
                               matrix[i][j-1] - 3)
    return matrix

def print_matrix(seq1, seq2):
    matrix = build_matrix(seq1, seq2)
    print("   "),
    for i in range(len(seq1)):
        print("  %s" % seq1[i]),
    print
    for i in range(len(matrix[0])):
        print("  %s" % seq2[i]),
        for j in range(len(matrix)):
            print('%3d' % matrix[j][i]),
        print
    #sequence_comparison(seq1, seq2)
    #print("%s\n%s" % sequence_comparison(seq1, seq2))

def global_max(matrix):
    max_ij = []
    #max_j = []
    max_val = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_ij = [(i, j)]
                #max_j = [j]
            elif matrix[i][j] == max_val:
                max_ij.append((i, j))
                #max_j.append(j)
    #return (max_i, max_j)
    return max_ij

def local_maxes(matrix):
    """Computes local maxes. keeping code for later but not going to be used
    in this"""
    local_max = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if(matrix[i-1][j-1] <= matrix[i][j] > matrix[i+1][j+1] and
               matrix[i-1][j] <= matrix[i][j] > matrix[i+1][j] and
               #matrix[i-1][j+1] <= matrix[i][j] > matrix[i+1][j-1] and
               matrix[i][j-1] <= matrix[i][j] > matrix[i][j+1]):

                local_max.append((i,j))

    for i in range(1, len(matrix) - 1):
        if(matrix[i-1][-1-1] <= matrix[i][-1] and
           matrix[i-1][-1] <= matrix[i][-1] > matrix[i+1][-1] and
           #matrix[i][-1] >= matrix[i+1][-1-1] and
           matrix[i][-1-1] <= matrix[i][-1]):

            local_max.append((i,j))

    for j in range(1, len(matrix[0]) - 1):
        if(matrix[-1-1][j-1] <= matrix[-1][j] and
           matrix[-1-1][j] <= matrix[-1][j] and
           #matrix[-1-1][j+1] <= matrix[-1][j] and
           matrix[-1][j-1] <= matrix[-1][j] > matrix[-1][j+1]):

            local_max.append((i,j))

    if(matrix[-2][-2] <= matrix[-1][-1] and
       matrix[-2][-1] <= matrix[-1][-1] and
       matrix[-1][-2] <= matrix[-1][-1]):

        local_max.append((len(matrix) - 1, len(matrix[0]) - 1))

    return local_max

def sequence_comparison(seqi, seqj, start=False):
    seqi = ''.join(['-', seqi])
    seqj = ''.join(['-', seqj])
    matrix = build_matrix(seqi, seqj)
    if start:
        maxes = global_max(matrix)
    else:
        maxes = global_max(matrix)
    #seqi_cor = []
    #seqj_cor = []
    seqi_cor = ''
    seqj_cor = ''
    max_seqs = []
    for i, j in maxes:
        seqi_cor = ''
        seqj_cor = ''
        while matrix[i][j] != 0:
            choices = [matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]]
            max_choice = max(choices)
            #if start:
               #print(matrix[i][j], i, j, seqi, seqj, matrix)
            if max_choice == choices[0] or seqi[i] == seqj[j]:
                seqi_cor = ''.join([seqi[i], seqi_cor])
                seqj_cor = ''.join([seqj[j], seqj_cor])
                i -= 1
                j -= 1
            elif max_choice == choices[1]:
                seqi_cor = ''.join(['-', seqi_cor])
                seqj_cor = ''.join([seqj[j], seqj_cor])
                j -= 1
            else:
                seqi_cor = ''.join([seqi[i], seqi_cor])
                seqj_cor = ''.join(['-', seqj_cor])
                i -= 1
        max_seqs.append((seqi_cor, seqj_cor))
    index = 0
    return max_seqs

def sequence_comparison_prev(seqi, seqj):
    matrix = build_matrix(seqi, seqj)
    local_max = local_maxes(matrix)
    removals = []
    for index, lmax in enumerate(local_max):
        if lmax[0] >= len(matrix) - 1 or lmax[1] >= len(matrix[0]) - 1:
            continue
        elif(seqi[lmax[0] + 1] == seqj[lmax[1]] or
             seqi[lmax[0]] == seqj[lmax[1] + 1]):
            if seqi[lmax[0] + 1] == seqj[lmax[1]]:
                local_max.append((lmax[0] + 1, lmax[1]))
            if seqi[lmax[0]] == seqj[lmax[1] + 1]:
                local_max.append((lmax[0], lmax[1] + 1))
            removals.insert(0, index)
    for index in removals:
        local_max.pop(index)
    

    pairs = []
    for start in local_max:
        i = start[0]
        j = start[1]
        pairs.append((seqi[i], seqj[j]))
        while matrix[i][j] != 0:
            print seqi[i], seqj[j]
            if matrix[i-1][j-1] >= max(matrix[i-1][j], matrix[i][j-1]):
                pairs[-1] = (''.join([seqi[i],pairs[-1][0]]),
                             ''.join([seqj[j],pairs[-1][1]]))
                i -= 1
                j -= 1
            #elif matrix[i-1][j] == matrix[i][j-1]:
                #recursively split the matrices?
            elif matrix[i-1][j] > matrix[i][j-1]:
                pairs[-1] = (''.join([seqi[i], pairs[-1][0]]), 
                             ''.join(['-', pairs[-1][1]]))
                i -= 1
            else:
                pairs[-1] = (''.join(['-', pairs[-1][0]]),
                             ''.join([seqj[j], pairs[-1][1]]))
                j -= 1
            print i, j
        print pairs
    for seq in pairs:
        print seq[0], '\n', seq[1]

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
            data.append(line.strip())
        print data
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)

    print sequence_comparison(data[0], data[1])
    #print_matrix(data[0], data[1])
    print sequence_comparison(data[1], data[0])
    #print global_max(build_matrix(data[0], data[1]))
    #print_matrix(data[1], data[0])
    #print global_max(build_matrix(data[1], data[0]))

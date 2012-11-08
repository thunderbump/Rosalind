#!/usr/bin/python
"""Performs Knuth-Morris-Pratt pre-processing on a sequence"""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """kmp.py [data file]
Performs Knuth-Morris-Pratt pre-processing on a sequence given in data file"""

def kmp_pp(seq):
    failure_ary = [0]
    index = 1
    border_width = 0
    while index < len(seq):
        if seq[index] == seq[border_width]:
            border_width += 1
            failure_ary.append(border_width)
            index += 1
        else:
            if border_width != 0:
                border_width = failure_ary[border_width - 1]
            else:
                failure_ary.append(0)
                index += 1
    return failure_ary

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]

    try:
        data_file = open(data_file_loc)
        sequence = data_file.readline().strip()
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)
    for failure in kmp_pp(sequence):
        print(failure),

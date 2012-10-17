#!/usr/bin/python
"""Finds reversal difference between sets of two permutations given in a data file"""

import sys
import string

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """rear.py [data file]
Finds reversal difference between sets of two permutations given in a data fi
le"""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    data_file_loc = sys.argv[1]

try:
    source_perms = []
    dest_perms = []
    data_file = open(data_file_loc)
    for index, line in enumerate(data_file):
        if line[-1] == '\n':
            line = line[:-1]
        if line:
            if line[-1] == '\r':
                line = line[:-1]
        if index % 3 == 0:
            perm = []
            for num in line.split(" "):
                perm.append(int(num))
            source_perms.append(perm)
        if index % 3 == 1:
            perm = []
            for num in line.split(" "):
                perm.append(int(num))
            dest_perms.append(perm)
except IOError, error:
    print(error)
    print(usage)
    sys.exit(1)

source_perm = source_perms[0]
dest_perm = dest_perms[0]
max_depth = len(source_perms[0]) - 1
if source_perm != dest_perm:
    for index in range(0, len(source_perm) - 1):
        for subindex in range(index + 1, len(source_perm)):
            print source_perm[index:subindex][::-1]

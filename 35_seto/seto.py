#!/usr/bin/python
"""Computes union and intersection of two sets, as well as each set subtracted
from eachother, and the compliment of each against a universe"""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """seto.py [data_file]
Computes union and intersection of two sets, as well as each set subtracted
from eachother, and the compliment of each against a universe"""

def print_set(stuff):
    if not stuff:
        print("set must exist")
        return
    if len(stuff) == 0:
        print("set must not be empty")
        return
    print("{%d," % stuff[0]),
    for thing in stuff[1:-1]:
        print("%d," % thing),
    print("%d}" % stuff[-1])
    return

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]
    try:
        data_file = open(data_file_loc)
        u = range(1, int(data_file.readline().strip()) + 1)
        a_raw = data_file.readline().strip()[1:-1]
        b_raw = data_file.readline().strip()[1:-1]
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)
    except ValueError:
        print("Malformed data file: Universe must be an integer > 1")
        sys.exit(1)
    try:
        a = []
        for index in a_raw.split(","):
            a.append(int(index))
    except ValueError:
        print("Malformed data file: Set A must contain numeric members")
    try:
        b = []
        for index in b_raw.split(","):
            b.append(int(index))
    except ValueError:
        print("Malformed data file: Set B must contain numeric members")
    print_set(list(set(a).union(set(b))))
    print_set(list(set(a).intersection(set(b))))
    print_set(list(set(a) - set(b)))
    print_set(list(set(b) - set(a)))
    print_set(list(set(u) - set(a)))
    print_set(list(set(u) - set(b)))

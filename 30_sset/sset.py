#!/usr/bin/python
"""Counts the number of subsets in a set of size X % 1,000,000"""

import sys

argc = len(sys.argv)
usage = """sset.py X
Counts the number of subsets in a set of size X"""

def num_subsets(X):
    return 2 ** X

if __name__ == "__main__":
    if argc != 2:
        print(usage)
        sys.exit(1)
    try:
        print(num_subsets(int(sys.argv[1])) % 1000000)
    except ValueError:
        print(usage)
        print("X must be an integer")
        sys.exit(1)

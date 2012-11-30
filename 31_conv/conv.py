#!/usr/bin/python
"""Finds the highest multiplicity of the Minkowski difference of two sets."""

import sys
from decimal import * 

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """conv.py [data_file]
Finds the highest multiplicity of the Minkowski difference of two sets."""

def m_sum(set_1, set_2):
    ret_sum = []
    for thing in set_1:
        for other_thing in set_2:
            ret_sum.append(thing + other_thing)
    return ret_sum

def m_diff(set_1, set_2):
    ret_diff = []
    for thing in set_1:
        for other_thing in set_2:
            ret_diff.append(abs(thing - other_thing))
    return ret_diff

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]
    try:
        data_file = open(data_file_loc)
        a = list(Decimal(thing) for thing in data_file.readline().strip().split())
        b = list(Decimal(thing) for thing in data_file.readline().strip().split())
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)
    except ValueError, error:
        print(usage)
        print("Malformed data file: %s" % error)
        sys.exit(1)

    m = m_diff(a, b)
    multiplicity = {}
    while len(m) != 0:
        s = m.pop()
        if multiplicity.has_key(s):
            multiplicity[s] += 1
        else:
            multiplicity[s] = 1
    max_multiplicity = 0
    max_key = None
    for thing in multiplicity.keys():
        if multiplicity[thing] > max_multiplicity:
            max_multiplicity = multiplicity[thing]
            max_key = thing
    print(max_multiplicity)
    print("%.5f" % max_key)

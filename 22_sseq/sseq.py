#!/usr/bin/python
"""Finds all indices of the intersection of a substring inside of another 
string"""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """sseq.py [data file]
Finds all indices of the intersection of a substring inside of another
string drawn from a common data file. If no data file is provided, test_data
is assumed."""

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]

    try:
        data_file = open(data_file_loc)
        sup_str = data_file.readline().strip()
        sub_str = data_file.readline().strip()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)

    intersect_locations = []
    sup_str_index = 0
    sub_str_index = 0
    while sub_str_index < len(sub_str):
        while sup_str_index < len(sup_str):
            if sub_str[sub_str_index] == sup_str[sup_str_index]:
                intersect_locations.append(sup_str_index + 1)
                sup_str_index += 1
                break
            else:
                sup_str_index += 1
        sub_str_index += 1
    for location in intersect_locations:
        print(location),

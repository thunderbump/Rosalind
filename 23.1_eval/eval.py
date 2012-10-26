#!/usr/bin/python
"""Computes the probability of a sequence of a given length to exist in another
sequence of a different given length with a given GC-content"""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """eval.py [data file]
Computes the probability of a sequence of a given length to exist in another
sequence of a different given length with a given GC-content"""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    data_file_loc = sys.argv[1]

try:
    data_file = open(data_file_loc)
    substring_info = data_file.readline()
    gc_info = data_file.readline()
    if substring_info[-1] == '\n':
        substring_info = substring_info[:-1]
    if substring_info[-1] == '\r':
        substring_info = substring_info[:-1]
    if gc_info[-1] == '\n':
        gc_info = gc_info[:-1]
    if gc_info[-1] == '\r':
        gc_info = gc_info[:-1]
    [substr_len_str, supstr_len_str] = substring_info.split(' ')
    gc_vals_str = gc_info.split(' ')
    substring_len = int(substr_len_str)
    supstring_len = int(supstr_len_str)
    gc_vals = []
    for val in gc_vals_str:
        gc_vals.append(float(val))
    print substring_len, supstring_len, gc_vals
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)
except ValueError:
    print("Corrupt DB.")
    sys.exit(1)
#wrong...way wrong. need my books :P
for gc_value in gc_vals:
    pgc = gc_value / 2
    pat = (1 - gc_value) / 2
    p_identical_char = 2 * (pgc ** 2) + 2 * (pat ** 2)
    p_substring = p_identical_char ** substring_len
    p_substring_exists = 1 - (p_substring ** (supstring_len - substring_len))
    print(p_substring_exists, p_substring, p_identical_char)

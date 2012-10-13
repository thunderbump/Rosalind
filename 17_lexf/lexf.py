#!/usr/bin/python

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """lexf.py [data file]"""

if argc > 2:
    sys.exit(1)
if argc == 2: 
    data_file_loc = sys.argv[1]

try:
    data_file = open(data_file_loc)
    alphabet = data_file.readline()[::2]
    depth = int(data_file.readline())
    data_file.close()
except IOError, error:
    print(error)
    sys.exit(1)

def enum(prev_string, cur_depth):
    if cur_depth <= 0:
        print(prev_string)
        return
    for char in alphabet:
        enum(''.join([prev_string, char]), cur_depth - 1)

try:
    enum('', depth)
except:
    print("depth too big")
    sys.exit(1)

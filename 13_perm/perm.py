#!/usr/bin/python

import sys
import math

argc = len(sys.argv)
data = '3'
usage = """perm.py [x]
counts and displays all permutations in the set {y | 0 < y <= x & y in Integers}"""
data_set = []

if argc > 2:
    print(usage)
if argc == 2:
    data = sys.argv[1]
try:
    for x in range(1, int(data) + 1):
        data_set.append(str(x))
except:
    print("Argument must be numeric")

def permute(remaining_set, prev_string):
    if prev_string == '':
        print(math.factorial(len(remaining_set)))
    #print remaining_set
    #print prev_string
    if(len(remaining_set) == 0):
        print(prev_string[1:])
    else:
        for element in remaining_set:
            permute(remaining_set.difference(element), 
                    ' '.join([prev_string, element]))

permute(set(data_set), '')

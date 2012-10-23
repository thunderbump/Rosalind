#!/usr/bin/python
"""Finds reversal difference between sets of two permutations given in a data file"""

import sys
import string
import ast
import random

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """rear.py [data file]
Finds reversal difference between sets of two permutations given in a data fi
le"""
base_perm = [1,2,3,4,5,6,7,8,9,10]
build = False

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

def permute(source, path_str="", depth=0, visited={}):
    #print depth
    #source_perm = source_perms[0]
    #dest_perm = dest_perms[0]
    if not visited.has_key(str(source)):
        visited[str(source)] = depth
        #for key in visited.keys():
        #    if key == source:
        #        print "wtf\n%s\n%s" % (source, key)
        #        raw_input()
    else:
        if visited[str(source)] > depth:
            visited[str(source)] = depth
        else:
            return visited
#        print("!"),
        #else:
        #    return visited
    if depth >= len(source):
    #if depth >= len(source) - 1:
    #if depth >= 5:
        return visited
    max_depth = len(source) - 1
    for start_index in range(0, len(source) - 1):
        if depth < 5:
            print(" ".join([path_str, str(start_index)]))
        for end_index in range(start_index + 2, len(source) + 1):
            next_step = source[:start_index]
            for item in source[start_index:end_index][::-1]:
                next_step.append(item)
            for item in source[end_index:]:
                next_step.append(item)
            if depth >= 5:
                permute(next_step, "", depth + 1, visited)
            else:
                permute(next_step, " ".join([path_str, str(start_index)]),
                        depth + 1, visited)
               
    return visited
        
#print sum(a for a in source_perms[0])
reference_file = open("dict_reference", 'r')
try:
#    saved_dict = ast.literal_eval(reference_file.readline())
    saved_dict = eval(reference_file.readline())
except:
    saved_dict = {}
reference_file.close()

if build:
    reference_file = open("dict_reference", 'w')
    reference_file.write(str(permute(base_perm, "", 0, saved_dict)))
    reference_file.close()


for index, perm in enumerate(source_perms[1:]):
    perm_trans = {}
    index_trans = {}
    for perm_index, item in enumerate(perm):
        perm_trans[item] = perm_index + 1
        index_trans[perm_index + 1] = item
    #for char in dest_perms[index]:
    #    print "%r" % char
    #print perm_trans, index_trans
    print(saved_dict[str(list(perm_trans[item] for item in dest_perms[index]))]),

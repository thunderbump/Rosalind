#!/usr/bin/python
"""Prints all signed permutations of a given length X"""

import sys

argc = len(sys.argv)
usage = """sign.py [X]
Prints all signed permutations of a given length X"""
#all wrong remake
def permute(target_list):
    print target_list
    return_list = []
    if len(target_list) == 1:
        return target_list
    for index in range(0, len(target_list)):
        choice = target_list[index]
        tmp_list = list(target_list)
        tmp_list.pop(index)
        tmp_list = permute(tmp_list)
        print tmp_list
        for thing in tmp_list:
            thing.insert(choice, 0)
        print choice
    print tmp_list
    return tmp_list


if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        try:
            X = int(sys.argv[1])
        except ValueError:
            print(usage)
            print("X must be numeric")
            sys.exit(1)
    source_list = range(1, X+1)
    permute(source_list)


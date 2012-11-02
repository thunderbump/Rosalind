#!/usr/bin/python
"""Prints all signed permutations of a given length X"""

import sys

argc = len(sys.argv)
usage = """sign.py [X]
Prints all signed permutations of a given length X"""

def permute(target_list):
    return_list = []
    if len(target_list) == 1:
        return_list.append(target_list)
        return return_list
    for index in range(0, len(target_list)):
        choice = target_list[index]
        sent_list = []
        for sub_index in range(0, len(target_list)):
            if sub_index != index:
                sent_list.append(target_list[sub_index])
        received_list = permute(sent_list)
        for sublist in received_list:
            sublist.insert(0, choice)
            return_list.append(sublist)
    return return_list

def sign_permute(target_list):
    returned_perms = []
    index = 0
    while index < 2 ** len(target_list):
        scratch_list = list(target_list)
        for bit_index, element in enumerate(target_list):
            if index & (2 ** bit_index) != 0:
                scratch_list[bit_index] *= -1
        returned_perms.append(scratch_list)
        index += 1
    return returned_perms


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
    raw_perms = permute(source_list)
    signed_perms = []
    for element in raw_perms:
        for signed_perm in sign_permute(element):
            signed_perms.append(signed_perm)
    print(len(signed_perms))
    for perm in signed_perms:
        for value in perm:
            print(value),
        print
            

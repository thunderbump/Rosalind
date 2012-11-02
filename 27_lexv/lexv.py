#!/usr/bin/python
"""Enumerates all strings of length less than some integer N from a given
alphabet. Both given in a data file"""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """lexv.py [data file]
Enumerates all strings of length less than some integer N from a given
alphabet. Both given data file, or "test_data" if no data file provided"""

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]

    try:
        data_file = open(data_file_loc)
        alphabet = data_file.readline()
        N = int(data_file.readline())
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)
    except ValueError:
        print(usage)
        print("Corrupt data file. N must be numeric")
        sys.exit(1)

    #bwuuh newlines
    if alphabet[-1] == '\n':
        alphabet = alphabet[:-1]
    if alphabet[-1] == '\r':
        alphabet = alphabet[:-1]
    alphabet = ''.join(alphabet.split(' '))
#    if N[-1] == '\n':
#        N = N[:-1]
#    if N[-1] == '\r':
#        N = N[:-1]
    ###############
    
    all_mers = []
    all_kmers = ['']
    for letter in alphabet:
        all_mers.append(letter)
    for index in range(0, N):
        scratch = []
        for string in all_kmers:
            for letter in alphabet[::-1]:
                scratch.append(''.join([string, letter]))
                if string == '':
                    continue
                all_mers.insert(all_mers.index(string) + 1,
                                    ''.join([string, letter]))
        all_kmers = scratch
#    print all_kmers
    for thing in all_mers:
        print thing

#!/usr/bin/python
"""Finds the protein string corrisponding to the prefix spectrums given in a
data file."""

import sys
import math

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """spec.py [data file]
Finds the protein string corrisponding to the prefix spectrums given in a
data file."""
#weight_dict = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
#'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496,
#'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858,
#'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931,
#'Y': 163.06333}

weight_dict = {71.03711: 'A', 103.00919: 'C', 115.02694: 'D', 129.04259: 'E',
147.06841: 'F', 57.02146: 'G', 137.05891: 'H', 113.08406: 'I', 128.09496: 'K',
113.08406: 'L', 131.04049: 'M', 114.04293: 'N', 97.05276: 'P', 128.05858: 'Q',
156.10111: 'R', 87.03203: 'S', 101.04768: 'T', 99.06841: 'V', 186.07931: 'W',
163.06333: 'Y'}
weights = weight_dict.keys()


def prefix_to_sequence(sequence):
    index = 0
    max_idx = len(sequence) - 1
    found_sequence = ''
    while index < max_idx:
        test = abs(sequence[index] - sequence[index + 1])
        closest = 0
        for weight in weights:
            if abs(test - weight) < abs(test - closest):
                closest = weight
        index += 1
        found_sequence = ''.join([found_sequence, weight_dict[closest]])
    return found_sequence

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]
    
    try:
        prefix_weights = []
        data_file = open(data_file_loc)
        for line in data_file:
            prefix_weights.append(float(line.strip()))
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)
    except ValueError:
        print(usage)
        print("data file corrupt")
        sys.exit(1)
    
    print prefix_to_sequence(prefix_weights)

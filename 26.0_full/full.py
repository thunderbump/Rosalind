#!/usr/bin/python
"""Computes a genetic sequence from a series of masses from a mass 
spectrometer"""

import sys

argc = len(sys.argv)
usage = """full.py [data file]
Computes a genetic sequence from a series of masses from a mass
spectrometer, given in data file(or test_data if no data file given"""
data_file_loc = "test_data"
weight_dict = {71.03711: 'A', 103.00919: 'C', 115.02694: 'D', 129.04259: 'E',
147.06841: 'F', 57.02146: 'G', 137.05891: 'H', 113.08406: 'I', 128.09496: 'K',
113.08406: 'L', 131.04049: 'M', 114.04293: 'N', 97.05276: 'P', 128.05858: 'Q',
156.10111: 'R', 87.03203: 'S', 101.04768: 'T', 99.06841: 'V', 186.07931: 'W',
163.06333: 'Y'}

def analyze_spec(parent, ions):
    pairs = []
    index = 0
    while index < len(ions)/2:
        closest_partner = 0
        distance = 400
        for ion in ions:
            if abs(parent - ions[index] - ion) < distance:
                closest_partner = ion
                distance = abs(parent - ions[index] - ion)
        pairs.append((ions[index], closest_partner))
        index += 1
    index = 0
    sequence = ''
    while index < len(ions)/2-1:
        nearest_candidate = None
        tolerance = 1
        for candidate in weight_dict.keys():
            if round(abs(pairs[index + 1][0] - pairs[index][0] 
                         - candidate), 3) == 0:
                tolerance = abs(pairs[index + 1][0] - pairs[index][0] 
                                - candidate)
                nearest_candidate = candidate
        if not nearest_candidate:
            pairs[index + 1] = (pairs[index + 1][1], pairs[index + 1][0])
            pairs.sort()
            index = 0
            sequence = ''
        else:
            sequence = ''.join([sequence, weight_dict[nearest_candidate]])
            index += 1
    print sequence

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]
    try:
        data_file = open(data_file_loc)
        parent_weight = float(data_file.readline().strip())
        data = []
        for line in data_file:
            data.append(float(line.strip()))
        if parent_weight <= max(data):
            raise ValueError("Malformed Data File")
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)
    except ValueError, error:
        print(usage)
        print(error)
        sys.exit(1)

    analyze_spec(parent_weight, data)

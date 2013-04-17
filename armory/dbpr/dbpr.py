#!/usr/bin/python
import sys
from Bio import ExPASy
from Bio import SwissProt

GO_offset         = 0
proc_offset       = 2
proc_label_offset = 0
proc_crop_offset  = 2

usage = """dbpr.py uniprot_id
prints all biological process keywords associated with the given uniprot id"""

def get_keywords(lookup):
    try:
        handle = ExPASy.get_sprot_raw(lookup)
    except:
        print("Error in ExPASy")
        sys.exit(1)
    try:
        record = SwissProt.read(handle)
    except ValueError, error:
        print(error)
        sys.exit(1)
        
    for ref in record.cross_references:
        if ref[GO_offset] == 'GO':
            if ref[proc_offset][proc_label_offset] == 'P':
                print ref[proc_offset][proc_crop_offset:]

    return

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print(usage)
        sys.exit(1)
    get_keywords(sys.argv[1])
    sys.exit(0)


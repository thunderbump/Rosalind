#!/usr/bin/python

import sys
from Bio import Entrez, SeqIO

usage = """frmt.py GeneBank_ID_list
Given a space-separated list of GeneBank IDs, this will return the shortest
sequence in FASTA format."""
email_file_loc = "email"
db = "nucleotide"
rettype = "fasta"
FASTA_line_len = 70

try:
    email_file = open(email_file_loc)
    email = email_file.readline().strip()
except IOError, error:
    print(error)
    sys.exit(1)
Entrez.email = email

if __name__ == "__main__":
    argc = len(sys.argv)
    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)

    ids = sys.argv[1:]
    handle = Entrez.efetch(db = db, id = ids, rettype = rettype)
    records = list(SeqIO.parse(handle, rettype))
    records.sort(key=lambda rec: len(rec.seq))
    print("".join([">", records[0].description]))
    seq = records[0].seq
    while(len(seq) > FASTA_line_len):
        print(seq[0:FASTA_line_len])
        seq = seq[FASTA_line_len:]
    print(seq)

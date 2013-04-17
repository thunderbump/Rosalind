#!/usr/bin/python
import sys
from Bio import Entrez

email_file_loc = 'email'
argc = len(sys.argv)
usage = """gbk.py genus beginning_date end_date
Gives the number of GeneBank entries for the given genus between the given dates. Dates must be in
YYYY/MM/DD format"""


def date_lookup(organism, beg_date, end_date):
    try:
        email_file = open(email_file_loc)
        email = email_file.readline().strip()
    except IOError, error:
        print(error)
        sys.exit(1)
    
    database = "nucleotide"
    Entrez.email = email
    handle = Entrez.esearch(db=database, term=''.join([organism, "[Organism] AND ",
                            beg_date, ':', end_date, "[Publication Date]"]))
    record = Entrez.read(handle)
    print(record['Count'])
    return


if __name__ == "__main__":
    if argc != 4:
        print(usage)
        sys.exit(1)
    date_lookup(sys.argv[1], sys.argv[2], sys.argv[3])



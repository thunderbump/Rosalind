#!/usr/bin/python
import sys
from Bio import Entrez

email_file_loc = 'email'
argc = len(sys.argv)
usage = """pbmd.py surname initials year
Gives the PMID of the first article written by someone of the given surname in
the given Year"""


def article_lookup(surname, initials, year):
    try:
        email_file = open(email_file_loc)
        email = email_file.readline().strip()
    except IOError, error:
        print(error)
        sys.exit(1)
    
    max_listings = 400 #Hopefully people aren't publishing more than a journal
                       #a day
    database = "pubmed"
    Entrez.email = email
    handle = Entrez.esearch(db=database, retmax=max_listings, term=''.join([ \
                            surname, " ", initials,  "[Author] AND ", year,  \
                            "[Date - Publication]"]))
    record = Entrez.read(handle)
    print(record['IdList'][-1])
    return


if __name__ == "__main__":
    if argc != 4:
        print(usage)
        sys.exit(1)
    article_lookup(sys.argv[1], sys.argv[2], sys.argv[3])



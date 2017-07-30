import sys
from Bio import ExPASy
from Bio import  SwissProt

if __name__ == '__main__':
    f = open('rosalind_dbpr.txt', 'r')
    prot_id = f.readline()
    prot_id = str(prot_id)
    rec = SwissProt.read(ExPASy.get_sprot_raw("B7USC9"))
    gos = [r[2].split(':')[1] for r in rec.cross_references if r[0] == 'GO' and r[2].startswith('P')]
    print('\n'.join(gos))

from sys import argv
from Bio import Entrez
from Bio import SeqIO

def get_nuc_fasta(nucleotide_ids):
    Entrez.email = "email@email.com"
    handle = Entrez.efetch(db="nucleotide", id=[nucleotide_ids], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))

    shortest = min(records, key=lambda x: len(x.seq))
    print shortest.format('fasta')


def main():
    with open(argv[1], 'r') as inf:
        data = inf.read()

    nucleotide_ids = ', '.join(data.strip().split())
    get_nuc_fasta(nucleotide_ids)


if __name__ == "__main__":
    main()

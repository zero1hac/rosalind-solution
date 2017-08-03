from Bio import Entrez

def genbank(genus, dtstart, dtend):
        Entrez.email = "adelq@sas.upenn.edu"
        term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (genus, dtstart, dtend)
        handle = Entrez.esearch(db="nucleotide", term=term)
        record = Entrez.read(handle)
        return record["Count"]

if __name__ == "__main__":
    genus  = raw_input().strip()
    date1 = raw_input().strip()
    date2 = raw_input().strip()
    print genbank(genus, date1, date2)

dict1 = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'ACU': 'T', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': 'Stop', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'GAA': 'E', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'UGA': 'Stop', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGA': 'R', 'GCU': 'A', 'UAG': 'Stop', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

file1 = open('rosalind_prot.txt', 'r')
t = file1.readline().strip()
i = 0
result = ''
while i<len(t):
	if dict1[t[i:i+3]]=='Stop':
		i+=3
		continue
	result += dict1[t[i:i+3]]
	i+=3
print result

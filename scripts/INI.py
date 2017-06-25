s = raw_input().strip()
from collections import Counter
s = list(s)
dct_count = dict(Counter(s))
print str(dct_count['A']), str(dct_count['C']), str(dct_count['G']), str(dct_count['T'])

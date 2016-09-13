import sys
import re
from collections import Counter
file_input = open(sys.argv[1], "rb")
string_input = file_input.readline()
counters = Counter(re.findall(r"\w+", string_input))
dic_counters = dict(counters)
for i in dic_counters.keys():
    print i, dic_counters[i]


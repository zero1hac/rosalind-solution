import sys
from collections import Counter
file_input = open(sys.argv[1], "rb")
string_input = file_input.readline().strip()
dic_counted = dict(Counter(string_input))
print dic_counted['A'],dic_counted['C'], dic_counted['G'], dic_counted['T']

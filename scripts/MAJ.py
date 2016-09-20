import sys
from collections import Counter
import operator
file_input = open(sys.argv[1], "rb")
string_input_list = file_input.readlines()
k, n = map(int,string_input_list[0].strip().split())
#print n,k
#print string_input_list
n_ = n / 2
for i in range(1, k+1):
    #print i
    array = map(int, string_input_list[i].strip().split())
    array_counter_dict = dict(Counter(array))
    num = max(array_counter_dict.iteritems(), key=operator.itemgetter(1))[0]
    if array_counter_dict[num] > n_:
        print num,
    else:
        print -1,


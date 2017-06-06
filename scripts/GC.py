input1 = open('rosalind_gc.txt','r')
lines = input1.readlines()
max_name = ''
curr_name = ''
curr_gc = 'T'
cont = 0
flag = 0
max_val = 0.00
lines.append('>Rosa')
lines.append('T')
for i in range(len(lines)):
	if 'Rosa' in lines[i]:
		cont = curr_gc.count('C') + curr_gc.count('G')
		val = (100.0*cont)/len(curr_gc)
		if val>max_val:
			max_val = val
			max_name = curr_name
		curr_gc = ''
		curr_name = lines[i][1:]
	else:
		curr_gc+=lines[i].strip()
print max_name
print "%.4f" % max_val

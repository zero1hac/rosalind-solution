input_file = open('input_hamm.txt','r')
lines = [i.strip() for i in input_file.readlines()]
print sum([1 if lines[0][i]!=lines[1][i] else 0 for i in range(len(lines[0]))])

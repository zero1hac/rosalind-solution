import sys
file_input = open(sys.argv[1], "rb")
lines = file_input.readlines()
k, n = map(int, lines[0].strip().split())
print k,n
print lines
for i in range(1,k+1):
    line = lines[i]
    flag = 0
    array_ = map(int, line.strip().split())
    print array_
    for j in range(n):
        if -1*array_[j] in array_[j:]:
            print j+1, array_.index(-1*array_[j]) + 1
            flag=1
    if flag==0:
        print -1

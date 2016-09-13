import sys
file1 = open("rosalind_bins.txt", "rb")
file1_lines = file1.readlines()

n = int(file1_lines[0])
m = int(file1_lines[1])
A = map(int, file1_lines[2].strip().split())
#Array is already sorted

def bins(ini, last, key):
    #print ini,last
    if ini>last:
        return -1
    mid = (ini+last)/2
    if A[mid] == key:
        return mid
    elif A[mid] > key:
        return bins(ini, mid-1, key)
    else:
        return bins(mid+1, last, key)


K = map(int,file1_lines[3].strip().split())
for i in K:
    temp_bins = bins(0,len(A) - 1, i)
    if temp_bins == -1:
        print -1,
    else:
        print temp_bins + 1,

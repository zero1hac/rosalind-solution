import sys
file_input = open(sys.argv[1], "rb")
lines = file_input.readlines()
string_input1 = lines[1].strip()
array_input1 = map(int, string_input1.split())
string_input2 = lines[3].strip()
array_input2 = map(int, string_input2.split())
def merge_proc(arr1, arr2):
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            print arr1[i],
            i+=1
        else:
            print arr2[j],
            j+=1
    if i==len(arr1):
        while j<len(arr2):
            print arr2[j],
            j+=1
    else:
        while i<len(arr1):
            print arr1[i],
            i+=1
merge_proc(array_input1, array_input2)

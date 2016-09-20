import sys
file_input = open(sys.argv[1], "rb")
string_input = file_input.readlines()[1].strip()
array_input = map(int, string_input.split())
def count_insertion_sort(arr):
    count =0 
    for i in range(1,len(arr)):
        k = i
        while k>0 and arr[k]<arr[k-1]:
            count+=1
            t = arr[k]
            arr[k] = arr[k-1]
            arr[k-1] = t
            k = k-1
    return count
print count_insertion_sort(array_input)

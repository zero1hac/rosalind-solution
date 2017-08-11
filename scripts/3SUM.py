def print_arr(A, j, val):
    dict1 = {}
    for i in range(j, len(A)):
        try:
            k = dict1[(val - A[i])]
            return (k, i)
        except:
            dict1[A[i]] = i
    return (-1,-1)

if __name__ == "__main__":
    k , n = map(int, raw_input().strip().split())
    for i in range(k):
        arr = map(int, raw_input().strip().split())
        flag=0
        for j in range(len(arr)-2):
            a, b = print_arr(arr, j+1, -1*arr[j])
            if a!=-1:
                print j+1, a+1, b+1
                flag=1
                break
        if not flag:
            print -1




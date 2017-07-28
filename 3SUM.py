def print_arr(A, j):
    dict1 = {}
    for i in range(j, len(A)):
        try:
            k = dict1[-1 * A[i]]
            return (k, i)
        except:
            dict1[A[i]] = i
    return (-1,-1)

if __name__ == "__main__":
    k , n = map(int, raw_input().strip().split())
    for i in range(k):
        arr = map(int, raw_input().strip().split())
        for k in range(len(arr)):



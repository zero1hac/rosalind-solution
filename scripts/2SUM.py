def print_arr(A):
    dict1 = {}
    for i in range(len(A)):
        try:
            k = dict1[-1 * A[i]]
            return (k, i)
        except:
            dict1[A[i]] = i
    return (-1,-1)

if __name__ == '__main__':
    n , m = map(int, raw_input().strip().split())
    for i in range(n):
        arr = map(int, raw_input().strip().split())
        t = print_arr(arr)
        if t[0]!=-1:
            print t[0]+1, t[1]+1
        else:
            print "-1"

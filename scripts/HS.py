import Queue as Q
q = Q.PriorityQueue()
n = int(raw_input().strip())
arr = map(int, raw_input().strip().split())
for i in range(n):
    q.put(arr[i])
for i in range(n):
    print q.get(),

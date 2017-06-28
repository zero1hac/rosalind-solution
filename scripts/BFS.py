import Queue
graph = {}
n, e = map(int, raw_input().strip().split())
for i in range(n):
    graph[i+1] = []
visited = [False]*n
for a in range(e):
    v1, v2 = map(int, raw_input().strip().split())
    graph[v1].append(v2)
    #graph[v2].append(v1)

level = [0]*n
q = Queue.Queue()
q.put(1)
visited[0] = True
def check_empty(q):
    r = Queue.Queue()
    print "Function",
    while not q.empty():
        t = q.get()
        print t,
        r.put(t)
    return r

while not q.empty():
    v = q.get()
    for i in graph[v]:
        if not visited[i-1]:
            visited[i-1] = True
            q.put(i)
            level[i-1] = level[v-1]+1
for i in range(n):
    if visited[i] == False:
        level[i] = -1
print ' '.join([str(i) for i in level])

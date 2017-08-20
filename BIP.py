class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
def check_bipartite(graph, src):
    V = len(graph)
    colors = [-1]*V

    colors[src] = 1
    q = Queue()
    q.enqueue(src)

    while not q.isEmpty():
        u = q.dequeue()
        #print colors
        for i in range(len(graph[u])):
            if colors[graph[u][i]]==-1:
                colors[graph[u][i]] = 1 - colors[u]
                q.enqueue(graph[u][i])
            elif colors[u] == colors[graph[u][i]]:
                return False
    return True

N = int(raw_input().strip())
for a0 in range(N):
    V, E = map(int , raw_input().strip().split())
    graph = []
    for i in range(V):
        graph.append([])
    for k in range(E):
        u,v = map(int, raw_input().strip().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #print graph
    if check_bipartite(graph, 0):
        print 1,
    else:
        print -1,

import Queue as Q
graph = {}
N, E = map(int, raw_input().strip().split())
for i in range(N):
    graph[i+1] = []

for i in range(E):
    x, y = map(int, raw_input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*N

def bfs(n):
    visited[n-1] = True
    queue = Q.Queue()
    queue.put(n)
    while not queue.empty():
        t = queue.get()
        for i in graph[t]:
            if not visited[i-1]:
                visited[i-1] = True
                queue.put(i)

component = 0

for i in range(1, N+1):
    #print visited, i
    if not visited[i-1]:
        visited[i-1] = True
        component+=1
        bfs(i)

print component





n,e = map(int, raw_input().strip().split())
graph = {}
for i in range(n):
	graph[i] = []
for a in range(e):
	v1, v2 = map(int, raw_input().strip().split())
	graph[v1-1].append(v2-1)
	#print graph
	graph[v2-1].append(v1-1)
#print graph
for a in range(n):
	count = 0
	for i in graph[a]:
		count+=len(graph[i])
	print count, 

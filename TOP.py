def read_graph():
    n, e = map(int, raw_input().strip().split())
    from_lists = [set() for _ in range(n)]
    to_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, raw_input().strip().split())
        from_lists[v2 - 1].add(v1 - 1)
        to_lists[v1 - 1].append(v2 - 1)
    return from_lists, to_lists

def dfs(from_lists, to_lists, visited, sequence, v):
    visited[v] = True
    sequence.append(v)
    for adj in to_lists[v]:
        if not visited[adj]:
            from_lists[adj].remove(v)
            if len(from_lists[adj]) == 0:
                dfs(from_lists, to_lists, visited, sequence, adj)

def topological_sort(from_lists, to_lists):
    visited = [False] * len(from_lists)
    sequence = []
    for i in range(len(visited)):
        if not visited[i] and len(from_lists[i]) == 0:
            dfs(from_lists, to_lists, visited, sequence, i)
    return sequence

def main():
    print ' '.join(map(lambda v: str(v + 1), topological_sort(*read_graph())))

if __name__ == '__main__':
    main()

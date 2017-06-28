import heapq
n = int(raw_input())
arr = map(int, raw_input().strip().split())
def heapify(heap, i):
    if i==0:
        return
    parent = (i - 1)/2
    child = i
    if heap[child] < heap[parent]:
        return
    else:
        heap[child], heap[parent] = heap[parent], heap[child]
        heapify(heap, parent)


heap = []
for i in range(n):
    heap.append(arr[i])
    heapify(arr, i)

print " ".join([str(i) for i in arr])

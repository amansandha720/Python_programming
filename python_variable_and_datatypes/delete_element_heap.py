import heapq

heap = [1,3,5,7,9]
heapq.heapify(heap)
smallest = heapq.heappop(heap)
print("Smallest: ",smallest)
print("Heap: ",heap)
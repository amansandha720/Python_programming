import heapq

heap = [1,3,5,7,9]
heapq.heapify(heap)

element_to_remove = 5
heap.remove(element_to_remove)
heapq.heapify(heap)
print(heap)
import heapq
from nodo import Node

def build_tree(freq):
    heap = [[weight, Node(char, wight)] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        merged_node = Node(None, lo[0] + hi[0])
        merged_node.left = lo[1]
        merged_node.right = hi[1]
        heapq.heappush(heap, [merged_node.frequency, merged_node])
    return heap[0][1]


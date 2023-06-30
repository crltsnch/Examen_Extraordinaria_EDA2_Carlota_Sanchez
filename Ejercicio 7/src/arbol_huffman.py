import heapq
from nodo import Node

def build_tree(freq):
    heap = [[weight, Node(char, weight)] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        merged_node = Node(None, lo[0] + hi[0])
        merged_node.left = lo[1]
        merged_node.right = hi[1]
        heapq.heappush(heap, [merged_node.frequency, merged_node])
    return heap[0][1]

def generate_codes(root, current_code, codes):
    if root.symbol:
        codes[root.symbol] = current_code
    else:
        generate_codes(root.left, current_code + "0", codes)
        generate_codes(root.right, current_code + "1", codes)
    
def compress(message, freq):
    huff_tree = build_tree(freq)
    codes = {}
    generate_codes(huff_tree, "", codes)
    encoded_message = "".join(codes[char] for char in message)
    return encoded_message

def decompress(encoded_message, freq):
    huff_tree = build_tree(freq)
    decoded_message = ""
    current_node = huff_tree
    for bit in encoded_message:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.symbol:
            decoded_message += current_node.symbol
            current_node = huff_tree
    return decoded_message
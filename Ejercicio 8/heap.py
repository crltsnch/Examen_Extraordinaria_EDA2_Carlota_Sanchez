class Heap:
    def __init__(self):
        self.heap = []
    
    def arribo_h(self, elemento):
        self.heap.append(elemento)
        self._sift_up(len(self.heap)-1)
    
    def _sift_up(self, index):
        while index > 0:
            parent = (index-1)//2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    
    def atencion_h(self):
        if len(self.heap) == 0:
            raise IndexError("El heap está vacío")
        
        elemento = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return elemento
    
    def _sift_down(self, index):
        size = len(self.heap)
        while index < size:
            child = 2 * index + 1
            if child >= size:
                break

            if child + 1 < size and self.heap[child+1] < self.heap[child]:
                child += 1
            
            if self.heap[child] < self.heap[index]:
                self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
                index = child
            
            else:
                break
            
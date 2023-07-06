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
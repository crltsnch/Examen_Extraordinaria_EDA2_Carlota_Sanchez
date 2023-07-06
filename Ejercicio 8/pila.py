class Pila:
    def __init__(self):
        self.pila = []
    
    def apilar(self, elemento):
        self.pila.append(elemento)
    
    def desapilar(self):
        if len(self.pila) == 0:
            raise IndexError("La pila está vacía")
        
        return self.pila.pop()
    
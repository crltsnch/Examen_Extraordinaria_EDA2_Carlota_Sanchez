class NodoArista(object):
    #Clase nodo arista
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

class NodoVertice(object):
    #Clase nodo vertice
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):
    #Clase grafo implementación lista de listas de adyaciencia
    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

class Arista(object):
    #Clase arista
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
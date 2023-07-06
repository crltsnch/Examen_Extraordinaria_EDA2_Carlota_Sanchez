from nodos import NodoArista, NodoVertice, Grafo, Arista
from estructuras import Heap, Pila

def camino_mas_corto(grafo, origen, destino):
    inf = float('inf')
    no_visitados = Heap(grafo.tamanio)

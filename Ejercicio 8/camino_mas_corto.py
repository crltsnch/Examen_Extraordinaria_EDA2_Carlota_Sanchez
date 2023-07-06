from nodos import NodoArista, NodoVertice, Grafo, Arista
from camino_mas_corto import tamanio


def camino_mas_corto(grafo, origen, destino):
    inf = float('inf')
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig


from nodos import NodoArista, NodoVertice, Grafo, Arista
from arbol_expansion_minima import tamanio
from heap import Heap
from pila import Pila


def camino_mas_corto(grafo, origen, destino):
    inf = float('inf')
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            no_visitados.arribo_h([aux, None], 0)
        else:
            no_visitados.arribo_h([aux, None], inf)
        aux = aux.sig

    while not no_visitados.heap_vacio():
        dato = no_visitados.atencion_h()
        camino.apilar(dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = no_visitados.buscar_h(aux.destino)
            if no_visitados.heap[pos][0] > dato[0] + aux.info:
                no_visitados.heap[pos][1][1] = dato[1][0].info
                no_visitados.cambiar_prioridad(pos, dato[0] + aux.info)
            
            aux = aux.sig

    return camino
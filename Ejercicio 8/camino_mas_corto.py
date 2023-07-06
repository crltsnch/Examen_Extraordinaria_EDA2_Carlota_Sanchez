from nodos import NodoArista, NodoVertice, Grafo, Arista
from camino_mas_corto import tamanio
from heap import Heap, arribo_h, atencion_h, heap_vacio, buscar_h
from pila import Pila, apilar, desapilar


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

    while not heap_vacio(no_visitados):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscar_h(no_visitados, aux.destino)
            if no_visitados.vector[pos][0] > dato[0] + aux.info:
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
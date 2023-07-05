from nodos import NodoArista, NodoVertice, Grafo, Arista
import random

def agregar_arista(grafo, origen, destino):
    if grafo.inicio is None:
        grafo.inicio = NodoVertice(origen)
        grafo.inicio.adyacentes.inicio = NodoArista(None, destino)
    
    else:
        actual = grafo.inicio
        while actual.sig is not None:
            actual = actual.sig
        actual.sig = NodoVertice(origen)
        actual.sig.adyacentes.inicio = NodoArista(None, destino)
    
    grafo.tamaño += 1

def imprimir_grafo(grafo):
    actual = grafo.inicio
    while actual is not None:
        print(f"Vertice: {actual.info}")
        arista_actual = actual.adyacentes.inicio
        while arista_actual is not None:
            print(f"Arista: {arista_actual.info}")
            arista_actual = arista_actual.sig
        actual = actual.sig


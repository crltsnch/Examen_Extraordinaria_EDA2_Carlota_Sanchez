from nodos import NodoArista, NodoVertice, Grafo, Arista
import random

def agregar_arista(grafo, origen, destino, costo):
    if grafo.inicio is None:
        grafo.inicio = NodoVertice(origen)
        grafo.inicio.adyacentes.inicio = NodoArista(costo, destino)
    
    else:
        actual = grafo.inicio
        while actual.sig is not None:
            actual = actual.sig
        actual.sig = NodoVertice(origen)
        actual.sig.adyacentes.inicio = NodoArista(costo, destino)
    
    grafo.tamanio += 1


def agregar_vertice(grafo, dato):
    nodo = NodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux

def tamanio(grafo):
    return grafo.tamanio

def imprimir_grafo(grafo):
    actual = grafo.inicio
    while actual is not None:
        print(f"Vertice: {actual.info}")
        arista_actual = actual.adyacentes.inicio
        while arista_actual is not None:
            print(f"Arista: {arista_actual.info} ")
            arista_actual = arista_actual.sig
        actual = actual.sig

def generar_grafo_planetas():
    grafo = Grafo(dirigido = False)
    planetas = ['Tierra', 'Knowhere', 'Zen-Whoberi', 'Vormir', 'Titán', 'Nidavellir', 'Planeta X', 'Sakaar', 'Asgard', 'Xandar', 'Geonosis', 'Utapau', 'Mustafar']
    
    for planeta in planetas:
        agregar_vertice(grafo, planeta)
    
    for origen in planetas:
        for destino in planetas:
            if origen != destino:
               costo = random.randint(1, 10)
               agregar_arista(grafo, origen, destino, costo)

    return grafo


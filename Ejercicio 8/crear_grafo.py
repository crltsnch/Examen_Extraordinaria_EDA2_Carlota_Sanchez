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
    
    grafo.tamanio += 1

def imprimir_grafo(grafo):
    actual = grafo.inicio
    while actual is not None:
        print(f"Vertice: {actual.info}")
        arista_actual = actual.adyacentes.inicio
        while arista_actual is not None:
            print(f"Arista: {arista_actual.info}")
            arista_actual = arista_actual.sig
        actual = actual.sig

def generar_grafo_planetas():
    grafo = Grafo(dirigido = False)
    planetas = ['Tierra', 'Knowhere', 'Zen-Whoberi', 'Vormir', 'Titán', 'Nidavellir', 'Planeta X', 'Sakaar', 'Asgard', 'Xandar', 'Geonosis', 'Utapau', 'Mustafar']
    for planeta in planetas:
        grafo.inicio = NodoVertice(planeta)
        grafo.tamanio += 1
    
    for i in range(grafo.tamanio):
        actual = grafo.inicio
        for j in range(i):
            actual = actual.sig
        for k in range(4):
            destino = actual.info
            while destino == actual.info:
                destino = random.choice(planetas)
            agregar_arista(grafo, actual.info, destino)
            agregar_arista(grafo, destino, actual.info)
    
    return grafo
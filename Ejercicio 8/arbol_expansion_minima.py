import sys
from nodos import NodoArista, NodoVertice, Grafo, Arista
from grafo_planetas import buscar_vertice, tamanio


def obtener_arbol_expansion_minima(grafo):
    bosque = [[grafo.inicio.info]]
    aristas = []
    adyacentes = grafo.inicio.adyacentes.inicio
    while adyacentes is not None:
        aristas.append([grafo.inicio.info, adyacentes.destino, adyacentes.info])
        adyacentes = adyacentes.sig
    
    while (len(bosque[0])//2) < tamanio(grafo)-1:
        menor = sys.maxsize
        menor_arista = None
        tipo = None

        for arista in aristas:
            origen = arista[0]
            destino = arista[1]

            if origen not in bosque[0] and destino in bosque[0]:
                if arista[2] < menor:
                    menor, menor_arista = arista[2], arista
                    tipo = True
            
            if origen in bosque[0] and destino not in bosque[0]:
                if arista[2] < menor:
                    menor, menor_arista = arista[2], arista
                    tipo = False
        
        if menor_arista is None:
            break

        aristas.remove(menor_arista)

        if len(bosque[0]) != 1:
            bosque[0] += [menor_arista[0], menor_arista[1]]
        else:
            bosque.pop()
            bosque.append([menor_arista[0], menor_arista[1]])

        aux = None
        if tipo:
            aux = buscar_vertice(grafo, menor_arista[0])

        adyacentes = aux.adyacentes.inicio
        while adyacentes is not None:
            aristas.append([aux.info, adyacentes.destino, adyacentes.info])
            adyacentes = adyacentes.sig
    
    return bosque

def imprimir_arbol_expansion_minima(arbol):
    if not arbol:
        print("El árbol de expansión mínima está vacío.")
        return
    
    print("Árbol de expansion mínima: ")
    for arista in arbol:
        if len(arista) >= 3:
            print(f"Arista: {arista[0]} - {arista[1]}")
        else:
            print("Error: La arista no tiene el formato esperado.")
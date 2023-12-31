from grafo_planetas import generar_grafo_planetas, imprimir_grafo, buscar_vertice, tamanio
from arbol_expansion_minima import obtener_arbol_expansion_minima, imprimir_arbol_expansion_minima
from camino_mas_corto import camino_mas_corto
from vertices_accesibles import obtener_vertices_alcanzables

def main():
    #Generar grafo de planetas
    grafo = generar_grafo_planetas()
    print("Grafo inicial: ")
    imprimir_grafo(grafo)
    print()

    #Obtener árbol de expansión mínima
    arbol = obtener_arbol_expansion_minima(grafo)
    print("Árbol de expansión mínima: ")
    imprimir_arbol_expansion_minima(arbol)
    print()

    #Obtener camino más corto
    origen_destino = [['Tierra', 'Vormir'], ['Knowhere', 'Titán'], ['Zen-Whoberi', 'Nidavellir']]
    for i, [origen, destino] in enumerate(origen_destino, 1):
        camino = camino_mas_corto(grafo, origen, destino)
        print(f"Camino más corto {i}: ")
        while not camino.pila_vacia():
            vertice = camino.desapilar()
            print(vertice.info)
        print()
    
    #Todos los planetas alcanzables desde Titán
    vertice_titan = buscar_vertice(grafo, 'Titán')
    vertices_alcanzables = obtener_vertices_alcanzables(grafo, vertice_titan)
    print("Planetas alcanzables desde Titán: ")
    for vertice in vertices_alcanzables:
        print(vertice)
    print()


if __name__ == "__main__":
    main()
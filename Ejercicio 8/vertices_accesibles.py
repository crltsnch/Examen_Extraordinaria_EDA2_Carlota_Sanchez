from grafo_planetas import buscar_vertice, tamanio

def obtener_vertices_alcanzables(grafo, vertice):
    vertices_alcanzados = []
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            vertices_alcanzados.append(vertice.info)

            adyacentes = vertice.adyacentes.inicio

            while adyacentes is not None:
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    vertices_alcanzados.extend(obtener_vertices_alcanzables(grafo, adyacente))
                adyacentes = adyacentes.sig
            
        vertice = vertice.sig
    
    return vertices_alcanzados
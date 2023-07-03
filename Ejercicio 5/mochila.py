def es_solucion(solucion, capacidad):
    #Determinar si el conjunto es solución
    total = 0
    for elemento in solucion:
        total = round(total + elemento[1], 2)
    if total == capacidad:
        return True
    else:
        return False


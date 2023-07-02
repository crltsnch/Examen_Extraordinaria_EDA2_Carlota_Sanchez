from pila import Pila

def hijo_sin_amor(mochila, objetos_sacados=0):
    if mochila.esta_vacia():
        return False, objetos_sacados
    
    objeto = mochila.desapilar()
    objetos_sacados += 1

    if objeto == "anillo de poder":
        return True, objetos_sacados
    
    return hijo_sin_amor(mochila, objetos_sacados)
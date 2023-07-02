from pila import Pila

def hijo_sin_amor(mochila, objetos_sacados=0):
    if mochila.esta_vacia():
        return False, objetos_sacados
    
    objeto = mochila.desapilar()
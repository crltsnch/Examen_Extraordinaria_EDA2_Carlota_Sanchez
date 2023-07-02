from hijo_sin_amor import *

def main():
    mochila = Pila()
    mochila.apilar("libro")
    mochila.apilar("anillo de poder")
    mochila.apilar("linterna")
    mochila.apilar("llaves")
    mochila.apilar("piedra preciosa")

    encontrado, objetos_sacados = hijo_sin_amor(mochila)

    if encontrado:
        print("Se encontró un anillo de poder!")
    else:
        print("No se encontró un anillo de poder")

    print(f"Objetos sacados: {objetos_sacados}")

if __name__ == "__main__":
    main()
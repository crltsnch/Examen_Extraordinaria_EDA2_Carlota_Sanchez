from mochila import *

def main():
    objetos = [['Amuleto de los Dioses', 12, 103],
                ['Espada del Sol', 23, 60], 
                ['Collar de la Luna', 11, 70],
                ['Reloj del Tiempo', 15, 5],
                ['Anillo de la Vida', 7, 15]]
    
    sol = []
    cap_max = 100

    for elemento in objetos:
        elemento.append(round(elemento[2]/elemento[1], 2))
    
    objetos.sort(key=lambda x: x[3], reverse=True)
    sol = mochila(objetos, cap_max)
    print(sol)

if __name__ == "__main__":
    main()
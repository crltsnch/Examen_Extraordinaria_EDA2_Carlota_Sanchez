from armaduras import Armadura

def main():
    armaduras = []

    # Agregar armaduras a la lista
    armaduras.append(Armadura("MK-8888", "Mark I"))
    armaduras.append(Armadura("MK-8889", "Mark V")) 
    armaduras.append(Armadura("MK-8890", "Mark XLII"))

    # Ejecutar el método calificación de cada objeto
    for armadura in armaduras:
        calificacion = armadura.calificacion()
        print(f"Calificación de {armadura.nombre}: {calificacion}")

if __name__ == "__main__":
    main()
from armaduras_controller import ArmadurasController

def main():
    controller = ArmadurasController()

    # Agregar armaduras
    controller.agregar_armadura("MK-8888", "Mark I")
    controller.agregar_armadura("MK-8889", "Mark V")
    controller.agregar_armadura("MK-8890", "Mark XLII")
    
    # Obtener calificación de armaduras
    calificacion_markI = controller.obtener_calificacion("MK-8888")
    print(f"Calificacion de MK-8888: {calificacion_markI}")

    calificacion_markV = controller.obtener_calificacion("MK-8889")
    print(f"Calificacion de MK-8889: {calificacion_markV}")

    calificacion_markXLII = controller.obtener_calificacion("MK-8890")
    print(f"Calificacion de MK-8890: {calificacion_markXLII}")

if __name__ == "__main__":
    main()
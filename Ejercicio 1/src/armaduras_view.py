from armaduras_controller import ArmadurasController

class ArmadurasView:
    def __init__(self):
        self.controller = ArmadurasController()

    def agregar_armadura(self, nombre, rango):
        self.controller.agregar_armadura(nombre, rango)
        print("Armadura agregada con éxito")
    
    def obtener_calificacion(self, nombre):
        calificacion = self.controller.obtener_calificacion(nombre)
        print(f"Calificación de {nombre}: {calificacion}")
        
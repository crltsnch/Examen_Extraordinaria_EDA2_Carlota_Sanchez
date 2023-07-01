from armaduras import Armadura

class ArmadurasController:
    def __init__(self):
        self.armaduras = {}
  
    def agregar_armadura(self, nombre, rango):
        armadura = Armadura(nombre, rango)
        self.armaduras[nombre] = armadura
    
    def obtener_armadura(self, nombre):
        return self.armaduras.get(nombre)
    
    def obtener_calificacion(self, nombre):
        armadura = self.obtener_armadura(nombre)
        if armadura:
            return armadura.calificacion()
        else:
            return "Armadura no encontrada"    
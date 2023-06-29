from .armaduras import Armadura

class ArmadurasController:
    def __init__(self):
        self.armaduras = {}
  
    def agregar_armadura(self, nombre, rango):
        armadura = Armadura(nombre, rango)
        self.armaduras[nombre] = armadura
    
    def obtener_armadura(self, nombre):
        return self.armaduras.get(nombre)
    
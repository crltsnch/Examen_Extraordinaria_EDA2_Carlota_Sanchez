class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"Armadura {self.nombre} creada con éxito")
    
    def calificacion(self):
        if self.rango == "Mark I":
            return "Baja"
        elif self.rango == "Mark II":
            return "Media"
        elif self.rango == "Mark III":
            return "Alta"
        else:
            return "Desconocida"
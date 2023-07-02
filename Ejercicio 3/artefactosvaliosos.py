class ArtefactosVAliosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print(f"Artefacto valioso {self.nombre} creado con éxito")
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Peso: {self.peso}, Precio: {self.precio}, Fecha de caducidad: {self.fecha_caducidad}"
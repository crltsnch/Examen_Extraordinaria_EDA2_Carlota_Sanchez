from .armaduras_controller import ArmadurasController

def main():
    controller = ArmadurasController()

    # Agregar armaduras
    controller.agregar_armadura("MK-8888", "Mark I")
    controller.agregar_armadura("MK-8889", "Mark V")
    controller.agregar_armadura("MK-8890", "Mark XLII")
    

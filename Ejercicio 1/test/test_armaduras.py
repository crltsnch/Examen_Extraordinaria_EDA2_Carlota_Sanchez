import unittest
from src.armaduras import ArmadurasController

class TestArmadurasController(unittest.TestCase):
    def test_agregar_armadura(self):
        controller = ArmadurasController()
        controller.agregar_armadura("MK-8888", "Mark I")
        controller.assertEqual(len(controller.armaduras), 1)
    
    def test_obtener_armadura_existente(self):
        controller = ArmadurasController()
        controller.agregar_armadura("MK-8888", "Mark I")
        
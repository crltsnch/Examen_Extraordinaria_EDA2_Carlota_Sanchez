import unittest
from ..src.armaduras_controller import ArmadurasController


class TestArmadurasController(unittest.TestCase):
    def test_agregar_armadura(self):
        controller = ArmadurasController()
        controller.agregar_armadura("MK-8888", "Mark I")
        self.assertEqual(len(controller.armaduras), 1)
    
    def test_obtener_armadura_existente(self):
        controller = ArmadurasController()
        controller.agregar_armadura("MK-8888", "Mark I")
        armadura = controller.obtener_armadura("MK-8888")
        self.assertIsNotNone(armadura)
        self.assertEqual(armadura.nombre, "MK-8888")
        self.assertEqual(armadura.rango, "Mark I")
    
    def test_obtener_armadura_no_existente(self):
        controller = ArmadurasController()
        armadura = controller.obtener_armadura("MK-9999")
        self.assertIsNone(armadura)
    
    def test_obtener_calificacion_existente(self):
        controller = ArmadurasController()
        controller.agregar_armadura("MK-8888", "Mark I")
        calificacion = controller.obtener_calificacion("MK-8888")
        self.assertEqual(calificacion, "Baja")
    
    def test_obtener_calificacion_no_existente(self):
        controller = ArmadurasController()
        calificacion = controller.obtener_calificacion("MK-9999")
        self.assertEqual(calificacion, "Armadura no encontrada")

if __name__ == "__main__":
    unittest.main()
import unittest
from src.armaduras import Armadura

class TestArmaduras(unittest.TestCase):
    def test_calificacion_armaduras(self):
        armaduras = []
        armaduras.append(Armadura("MK-8888", "Mark I"))
        armaduras.append(Armadura("MK-8889", "Mark II"))
        armaduras.append(Armadura("MK-8890", "Mark XLII"))
    
        for armadura in armaduras:
            calificacion = armadura.calificacion()
            self.assertIsNotNone(calificacion)
            self.assertIn(calificacion, ["Baja", "Media", "Alta", "Desconocida"])


if __name__ == "__main__":
    unittest.main()
import unittest
from src.armaduras import Armadura

class TestArmaduras(unittest.TestCase):
    def test_str_armaduras(self):
        armaduras = []
        armaduras.append(Armadura("MK-8888", "Mark I"))
        armaduras.append(Armadura("MK-8889", "Mark II"))
        armaduras.append(Armadura("MK-8890", "Mark XLII"))
    
        for armadura in armaduras:
            self.assertIsInstance(str(armadura), str)
            print(armadura)


if __name__ == "__main__":
    unittest.main()
from crear_armaduras import *
import unittest

class TestCrearArmaduras(unittest.TestCase):
    def test_generar_armaduras(self):
        armaduras = generar_armaduras()
        self.assertEqual(len(armaduras), 2000)
    
    def test_crear_tablas_hash(self):
        armaduras = generar_armaduras()
        tabla_codigo, tabla_legion = crear_tablas_hash(armaduras)

        self.assertEqual(len(tabla_codigo.keys()), len(set(armaduras)))
        self.assertEqual(len(tabla_legion.keys()), len(set(armaduras)))

        for armadura in armaduras:
            codigo_hash = armadura[-3:]
            legion_hash = armadura[:2]

            self.assertIn(armadura, tabla_codigo[codigo_hash])
            self.assertIn(armadura, tabla_legion[legion_hash])
    
  ∑
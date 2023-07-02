import unittest
from ..src.hijo_sin_amor import *

class TestHijosSinAmor(unittest.TestCase):
    def test_hijo_sin_amor_encuentra_anillo(self):
        mochila = Pila()
        mochila.apilar("libro")
        mochila.apilar("anillo de poder")
        mochila.apilar("linterna")
        mochila.apilar("llaves")
        mochila.apilar("piedra preciosa")

        encontrado, objetos_sacados = hijo_sin_amor(mochila)
        self.assertTrue(encontrado)
        self.assertEqual(objetos_sacados, 4)

    def test_hijo_sin_amor_no_encuentra_anillo(self):
        mochila = Pila()
        mochila.apilar("libro")
        mochila.apilar("linterna")
        mochila.apilar("llaves")
        mochila.apilar("piedra preciosa")

        encontrado, objetos_sacados = hijo_sin_amor(mochila)
        self.assertFalse(encontrado)
        self.assertEqual(objetos_sacados, 4)

if __name__ == "__main__":
    unittest.main()
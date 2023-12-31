from mochila import es_solucion, mochila
import unittest

class TestMochila(unittest.TestCase):
    def test_mochila_ejemplo(self):
        objetos = [['Amuleto de los Dioses', 12, 103],
                ['Espada del Sol', 23, 60], 
                ['Collar de la Luna', 11, 70],
                ['Reloj del Tiempo', 15, 5],
                ['Anillo de la Vida', 7, 15]]
        cap_max = 100

        sol_esperada = [['Reloj del Tiempo', 15, 5],
                        ['Anillo de la Vida', 7, 15],
                        ['Espada del Sol', 23, 60],
                        ['Collar de la Luna', 11, 70],
                        ['Amuleto de los Dioses', 12, 103]]
        sol_obtenida = mochila(objetos, cap_max)

        sol_esperada = sorted(sol_esperada, key=lambda x: x[0])
        sol_obtenida = sorted(sol_obtenida, key=lambda x: x[0])

        self.assertListEqual(sol_esperada, sol_obtenida)
    
    def test_mochila_sin_solucion(self):
        objetos = [['Amuleto de los Dioses', 12, 103],
                ['Esapada del Sol', 23, 60], 
                ['Collar de la Luna', 11, 70],
                ['Reloj del Tiempo', 15, 5],
                ['Anillo de la Vida', 7, 15]]
        cap_max = 5

        sol_esperada = []
        sol_obtenida = mochila(objetos, cap_max)

        self.assertListEqual(sol_esperada, sol_obtenida)
    
    def test_mochila_un_objeto(self):
        objetos = [['Amuleto de los Dioses', 12, 103]]
        cap_max = 20

        sol_esperada = [['Amuleto de los Dioses', 12, 103]]
        sol_obtenida = mochila(objetos, cap_max)

        self.assertListEqual(sol_esperada, sol_obtenida)
    
    def test_mochila_vacia(self):
        objetos = []
        cap_max = 100

        sol_esperada = []
        sol_obtenida = mochila(objetos, cap_max)

        self.assertListEqual(sol_esperada, sol_obtenida)

if __name__ == "__main__":
    unittest.main()
import unittest
from ..src.artefactosvaliosos import ArtefactoValioso

class TestArtefactosValiosos(unittest.TestCase):
    def test_mostrar_datos_ordenados(self):
        artefactos = []
        artefactos.append(ArtefactoValioso(20, "Conserva de frutas", 500, "2023-12-31"))
        artefactos.append(ArtefactoValioso(10, "Joyas antiguas", 1000, "2024-06-30"))
        artefactos.append(ArtefactoValioso(15, "Pintura famosa", 1500, "2023-08-15"))
        
        artefactos_ordenados = sorted(artefactos, key=lambda artefacto: artefacto.fecha_caducidad)

        for artefacto in artefactos:
            if artefacto.nombre == "Conserva de frutas":
                artefacto.precio = 600
        
        for artefacto in artefactos_ordenados:
            print(artefacto)

if __name__ == "__main__":
    unittest.main()
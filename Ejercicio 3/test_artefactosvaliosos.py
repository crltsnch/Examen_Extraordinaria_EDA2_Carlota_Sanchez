import unittest
from src.artefactosvaliosos import ArtefactoValioso

class TestArtefactosValiosos(unittest.TestCase):
    def test_mostrar_datos_ordenados(self):
        artefactos = []
        artefactos.append(ArtefactoValioso(20, "Conserva de frutas", 500, "31-12-2023"))
        artefactos.append(ArtefactoValioso(10, "Joyas antiguas", 1000, "30-06-2024"))
        artefactos.append(ArtefactoValioso(15, "Pintura famosa", 1500, "15-08-2023"))
        
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

        #Verificar que todos los elementos estén en las tablas
        for armadura in armaduras:
            codigo_hash = armadura[-3:]
            legion_hash = armadura[:2]

            self.assertIn(armadura, tabla_codigo[codigo_hash])
            self.assertIn(armadura, tabla_legion[legion_hash])
    
    def test_eliminar_armadura_desertor(self):
        armaduras = generar_armaduras()
        tabla_codigo, tabla_legion = crear_tablas_hash(armaduras)

        eliminar_armadura_desertor(tabla_codigo, tabla_legion)

        #Verificar que FN-2187 fue eliminado correctamente
        self.assertNotIn('FN-2187', tabla_legion.get('FN', []))
        self.assertNotIn('FN-2187', tabla_codigo.get('187', []))
    
    def test_obtener_armaduras_asalto(self):
        armaduras = generar_armaduras()
        tabla_codigo, tabla_legion = crear_tablas_hash(armaduras)

        armaduras_asalto = obtener_armaduras_asalto(tabla_codigo)

        #Verificar que todas las armaduras de asalto terminan en '781'
        for armadura in armaduras_asalto:
            self.assertEqual()
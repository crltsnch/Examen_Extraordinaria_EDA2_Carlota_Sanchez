from crear_armaduras import *
import unittest

class TestCrearArmaduras(unittest.TestCase):
    def test_generar_armaduras(self):
        armaduras = generar_armaduras()
        self.assertEqual(len(armaduras), 2000)
    
    def test_crear_tablas_hash(self):
        armaduras = generar_armaduras()
        tabla_codigo, tabla_legion = crear_tablas_hash(armaduras)

        #Verificar que todos los elementos estén en las tablas
        for armadura in armaduras:
            codigo_hash = armadura[-3:]
            legion_hash = armadura[:2]

            self.assertIn(armadura, tabla_codigo.get(codigo_hash, []))
            self.assertIn(armadura, tabla_legion.get(legion_hash, []))
    
        total_armaduras = len(armaduras)
        total_codigos = sum(len(armaduras) for armaduras in tabla_codigo.values())
        total_legiones = sum(len(armaduras) for armaduras in tabla_legion.values())

        self.assertEqual(total_codigos, total_armaduras)
        self.assertEqual(total_legiones, total_armaduras)

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
            self.assertTrue(armadura.endswith('781'))
    
    def test_obtener_armaduras_exploracion(self):
        armaduras = generar_armaduras()
        tabla_codigo, tabla_legion = crear_tablas_hash(armaduras)

        armaduras_exploracion = obtener_armaduras_exploracion(tabla_codigo)

        #Verificar que todas las armaduras de exploración terminan en '537'
        for armadura in armaduras_exploracion:
            self.assertTrue(armadura.endswith('537'))

    def test_obtener_armaduras_ct(self):
        armaduras = generar_armaduras()
        tabla_codigo, tabla_legion = crear_tablas_hash(armaduras)

        armaduras_ct = obtener_armaduras_ct(tabla_legion)

        #Verificar que todas las armaduras de la legión CT terminan en 'CT'
        for armadura in armaduras_ct:
            self.assertTrue(armadura.startswith('CT'))
            

if __name__ == "__main__":
    unittest.main()
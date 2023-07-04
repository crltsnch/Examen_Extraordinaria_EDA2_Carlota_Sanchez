import random

#Función para generar un código de armadura
def generar_codigo():
    legion = random.choice(['FL', 'TF', 'TK', 'CT', 'FN', 'FO'])
    digitos = random.randint(1000, 9999)
    return f'{legion}-{digitos}'

#Generar 2000 armaduras
def generar_armaduras():
    armaduras = []
    for i in range(2000):
        armadura = generar_armaduras()
        armaduras.append(armadura)
    return armaduras


#Crear las tablas hash encadenadas
def crear_tablas_hash(armaduras):
    tabla_codigo = {}
    tabla_legion = {}

    for armadura in armaduras:
        codigo_hash = armadura[-3:]
        legion_hash = armadura[:2]

        if codigo_hash not in tabla_codigo:
            tabla_codigo[codigo_hash] = []
        tabla_codigo[codigo_hash].append(armadura)

        if legion_hash not in tabla_legion:
            tabla_legion[legion_hash] = []
        tabla_legion[legion_hash].append(armadura)

    return tabla_codigo, tabla_legion

def eliminar_armadura_desertor(tabla_codigo, tabla_legion):
    if 'FN-2187' in tabla_legion.get('FN', []):
        tabla_legion['FN'].remove('FN-2187')
    
    codigo_hash = '187'
    if codigo_hash in tabla_codigo and 'FN-2187' in tabla_codigo[codigo_hash]:
        tabla_codigo[codigo_hash].remove('FN-2187')

def obtener_armaduras_asalto(tabla_codigo):
    armaduras_asalto = []
    for armaduras in tabla_codigo.values():
        for armadura in armaduras:
            if armadura[-3:] == '781':
                armaduras_asalto.append(armadura)
    
    return armaduras_asalto

def obtener_armaduras_exploracion(tabla_codigo):
    armaduras_exploracion = []
    for armaduras in tabla_codigo.values():
        for armadura in armaduras:
            if armadura[-3:] == '537':
                armaduras_exploracion.append(armadura)
    
    return armaduras_exploracion

import random

#Función para generar un código de armadura
def generar_armaduras():
    legion = random.choice(['FL', 'TF', 'TK', 'CT', 'FN', 'FO'])
    digitos = random.randint(1000, 9999)
    return f'{legion}-{digitos}'

#Generar 2000 armaduras
armaduras = []
for i in range(2000):
    armadura = generar_armaduras()
    armaduras.append(armadura)

#Crear las tablas hash encadenadas
tabla_codigo = {}
tabla_legion = {}

for armadura in armaduras:
    codigo_hash = armadura[-3:]
    legion_hash = armadura[:2]

    if codigo_hash in tabla_codigo:
        tabla_codigo[codigo_hash] = []
    tabla_codigo[codigo_hash].append(armadura)
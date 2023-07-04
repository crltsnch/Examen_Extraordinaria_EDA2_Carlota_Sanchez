from creararmaduras import generar_armaduras, crear_tablas_hash, eliminar_armadura_desertor, obtener_armaduras_asalto, obtener_armaduras_exploracion, obtener_armaduras_ct, obtener_armaduras_tf

def main():
    armaduras = generar_armaduras()
    tabla_codigo, tabla_legion = crear_tablas_hash(armaduras)
    
    eliminar_armadura_desertor(tabla_codigo, tabla_legion)

    armaduras_asalto = obtener_armaduras_asalto(tabla_codigo)
    armaduras_exploracion = obtener_armaduras_exploracion(tabla_codigo)
    armaduras_ct_hoth = obtener_armaduras_ct(tabla_legion)
    armaduras_tf_ironheart = obtener_armaduras_tf(tabla_legion)

    print("Armaduras generadas:")
    print(armaduras)

    print("\nTabla de armaduras por código:")
    print(tabla_codigo)

    print("\nTabla de armaduras por legión:")
    print(tabla_legion)

    print("\nArmaduras de asalto:")
    print(armaduras_asalto)

    print("\nArmaduras de exploración:")
    print(armaduras_exploracion)

    print("\nArmaduras de la legión CT para misión a Hoth:")
    print(armaduras_ct_hoth)

    print("\nArmaduras de la legión TF para misión a Ironheart:")
    print(armaduras_tf_ironheart)

if __name__ == "__main__":
    main()
def menu_hospitales(lista_de_hospitales):
    lista_de_hospitales.sort(key=lambda x: x.nombre)
    cantidad_de_hospitales_en_la_lista = len(lista_de_hospitales)
    print("\n____Institución Hospitalaria____\n")
    for i, hosp in enumerate(lista_de_hospitales, start=1):
        print(f"{i}. {hosp.nombre}")
    print("-------------------")
    print(f"{cantidad_de_hospitales_en_la_lista + 1}. Salir")


def menu_inicial():
    print("\n____MENU____")
    print("1. Añadir institución médica.")
    print("2. Seleccionar institución médica.")
    print("3. Exportar datos.")
    print("4. Salir")


def menu():
    print("\n____MENU____")
    print("1. Contratar médico.")
    print("2. Ingresar paciente")
    print("3. Mostrar relación de médicos contratados")
    print("4. Mostrar relación de pacientes.")
    print("5. Mostrar Resumen.")
    print("6. Cambiar / añadir institución hospitalaria.")
    print("7. Salir")


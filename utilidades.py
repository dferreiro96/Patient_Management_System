def validar_nombre(mensaje):
    while True:
        nombre = input(mensaje).title() .strip()
        if len(nombre) < 3 or any(c.isdigit() for c in nombre):
            print(
                "\nEl nombre debe tener más de 3 caracteres, y contener únicamente letras."
            )
            continue
        return nombre


def escoer_opcion(mensaje, opciones):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion not in opciones:
                print("\nFuera de rango")
                continue
            else:
                return opcion
        except ValueError:
            print("\nIntroduzca un número válido")


def pedir_edad(mensaje):
    while True:
        try:
            edad = int(input(mensaje))
            if edad < 0 or edad > 120:
                print("Introduzca un valor válido de edad (0-120).")
                continue
            return edad
        except ValueError:
            print("Introduzca un valor válido de edad.")


def pedir_texto(mensaje):
    nombre = input(mensaje).title().strip()
    return nombre


def convertir_a_diccionario(lista_de_hospitales):
    datos_para_json = []
    for hospital in lista_de_hospitales:
        diccionario_hospitales = {
            "Nombre": hospital.nombre,
            "Médicos": [],
            "Pacientes": [],
        }
        for medicos in hospital.lista_medicos:
            diccionario_hospitales["Médicos"].append(
                {"Nombre": medicos.nombre, "Especialidad": medicos.especialidad}
            )
        for pacientes in hospital.lista_pacientes:
            diccionario_hospitales["Pacientes"].append(
                {
                    "Nombre": pacientes.nombre,
                    "Edad": pacientes.edad,
                    "Afección": pacientes.enfermedad,
                    "Médico asignado": pacientes.medico_asignado.nombre
                    if pacientes.medico_asignado
                    else None,
                }
            )

        datos_para_json.append(diccionario_hospitales)
    return datos_para_json
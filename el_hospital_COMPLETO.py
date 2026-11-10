import csv
import json
import time


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def devolver_tipo(self):
        tipo = self.__class__.__name__
        return tipo

    def mostrar_info(self):
        return self.nombre


class Medico(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def __str__(self):
        return f"Dr(a). {self.nombre} ({self.especialidad})"

    def mostrar_info(self):
        print(f"Dr. {self.nombre} - {self.especialidad}")


class Paciente(Persona):
    def __init__(self, nombre, edad, enfermedad, medico_asignado):
        super().__init__(nombre, edad)
        self.enfermedad = enfermedad
        self.medico_asignado = medico_asignado

    def __str__(self):
        return f"{self.nombre}"

    def asignar_medico(self, medico):
        self.medico_asignado = medico

    def mostrar_info(self):
        if self.medico_asignado:
            print(
                f"\nPaciente: {self.nombre}, {self.edad} años. Afección: {self.enfermedad} - Médico asignado: {self.medico_asignado}"
            )
        else:
            print(f"\nPaciente: {self.nombre} - No tiene médico asignado")


class Hospital:
    def __init__(self, nombre):

        self.nombre = nombre
        self.lista_personas = []

    def validar_medico(self):
        while True:
            nombre = validar_nombre("\nIntroduzca el nombre del médico: ")
            if any(m.nombre == nombre for m in self.lista_personas):
                print("\nYa registrado previamente")
            else:
                return nombre

    def añadir_medico(self, nuevo_medico):
        self.lista_personas.append(nuevo_medico)
        print(f"\nSe ha contratado al {nuevo_medico}")

    def añadir_paciente(self, nuevo_paciente):
        self.lista_personas.append(nuevo_paciente)
        print(
            f"\nSe ha ingresado al paciente {nuevo_paciente}, {nuevo_paciente.edad} años, que acudió por: {nuevo_paciente.enfermedad}; y será atendido por {nuevo_paciente.medico_asignado}"
        )

    def validar_paciente(self):
        while True:
            nombre = validar_nombre("\nIntroduzca el nombre del paciente: ")
            if any(m.nombre == nombre for m in self.lista_personas):
                print("\nYa registrado previamente")
            else:
                return nombre

    def extraer_medicos_de_lista_personas(self):
        if not self.lista_personas:
            return []
        else:           
            lista_de_medicos = []
            for esc in self.lista_personas:
                if isinstance(esc, Medico):                   
                    lista_de_medicos.append(esc)
            return lista_de_medicos
            

    def extraer_pacientes_de_lista_personas(self):
        lista_de_pacientes = []
        for esc in self.lista_personas:
            if isinstance(esc, Paciente):
                lista_de_pacientes.append(esc)
        return lista_de_pacientes

    def mostrar_medico_ordenados_por_especialidad(self):
        lista_medicos = self.extraer_medicos_de_lista_personas()
        if not lista_medicos:
            print("\nNo se han contratado médicos todavía\n")
        else:
            lista_medicos.sort(key=lambda x: x.especialidad)
            for i, med in enumerate(lista_medicos, start=1):
                print(f"{i}. Nombre: {med.nombre} --- Especialidad: {med.especialidad}")
            print(f"\nTotal de médicos contratados: {len(lista_medicos)}")

    def lista_de_medicos(self):
        print("\n_____RESUMEN DE MÉDICOS______")
        print(f"\nHOSPITAL {self.nombre}\n")
        self.mostrar_medico_ordenados_por_especialidad()

    def mostrar_pacientes_ordenados_por_nombre(self):
        lista_pacientes = self.extraer_pacientes_de_lista_personas()
        if not lista_pacientes:
            print("\nNo se han ingresado pacientes todavía\n")
        else:
            ordenados = sorted(lista_pacientes, key=lambda x: x.nombre)
            for i, pac in enumerate(ordenados, start=1):
                print(
                    f"{i}. Nombre: {pac.nombre} - Edad: {pac.edad} años - Motivo de consulta: {pac.enfermedad} - Médico asignado: {pac.medico_asignado}"
                )
            print(f"\nTotal de pacientes ingresados: {len(lista_pacientes)}")

    def lista_de_pacientes(self):
        print("\n_____RESUMEN DE PACIENTES______")
        print(f"\nHOSPITAL {self.nombre}\n")
        self.mostrar_pacientes_ordenados_por_nombre()

    def mostrar_resumen(self):
        print("\n_____RESUMEN______")
        print(f"\nHOSPITAL {self.nombre}\n")
        print("Lista de médicos contratados")
        print("__________________________\n")
        self.mostrar_medico_ordenados_por_especialidad()
        print()
        print("\nLista de pacientes")
        print("____________________")
        self.mostrar_pacientes_ordenados_por_nombre()


def validar_especialidad_medica(nombre_del_medico):
    especialidad = validar_nombre(f"Introducir especialidad de {nombre_del_medico}: ")
    return especialidad


def convertir_a_diccionario(lista_de_hospitales: list):
    datos_para_json = []
    for hospital in lista_de_hospitales:
        diccionario_hospital = {"Nombre": hospital.nombre, "Personas": []}
        for persona in hospital.lista_personas:
            diccionario_personas = persona.__dict__.copy()
            diccionario_personas["Tipo"] = persona.devolver_tipo()
            if isinstance(persona, Paciente) and persona.medico_asignado:
                diccionario_personas["medico_asignado"] = persona.medico_asignado.nombre
            diccionario_hospital["Personas"].append(diccionario_personas)             
        datos_para_json.append(diccionario_hospital)
    return datos_para_json


def guardar_datos(lista_de_hospitales):
    datos = convertir_a_diccionario(lista_de_hospitales)
    with open("Datos_hospital.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


def exportar_datos(lista_de_hospitales: list):
    nombre_del_archivo = "Reporte_Global.csv"
    with open(nombre_del_archivo, mode="w", encoding="utf-8", newline="") as archivo:
        columnas = [
            "Hospital",
            "Clase",
            "Nombre",
            "Edad",
            "Especialidad/Afección",
            "Médico Asignado",
        ]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()

        for hospital in lista_de_hospitales:
            for persona in hospital.lista_personas:
                if isinstance (persona, Medico):
                    especialidad_afeccion = persona.especialidad
                    medico_asignado = "-"
                else:
                    especialidad_afeccion = persona.enfermedad
                    medico_asignado = persona.medico_asignado.nombre if persona.medico_asignado else "Ninguno"
                    
                escritor.writerow(
                    {
                        "Hospital": hospital.nombre,
                        "Clase": persona.devolver_tipo(),
                        "Nombre": persona.nombre,
                        "Edad": persona.edad,
                        "Especialidad/Afección": especialidad_afeccion,
                        "Médico Asignado": medico_asignado,
                    }
                )
           
        print(
            f"\nSe han exportado los datos correctamente al archivo llamado: {nombre_del_archivo}"
        )


def descargar_datos():
    try:
        with open("Datos_hospital.json", "r", encoding="utf-8") as archivo:
            datos_descargados = json.load(archivo)
            if datos_descargados:
                lista_de_hospitales = []
                for cada_diccionario in datos_descargados:
                    hospital = Hospital(cada_diccionario["Nombre"])
 
                    for cada_persona in cada_diccionario["Personas"]: #reconstruyendo medicos
                        if cada_persona["Tipo"] == "Medico":
                            medico = cada_persona["nombre"]
                            edad = cada_persona["edad"]
                            especialidad = cada_persona["especialidad"]
                            nuevo_medico = Medico(medico, edad, especialidad)
                            hospital.añadir_medico(nuevo_medico)

                        # reconstruyendo pacientes

                        else:
                            nuevo_paciente = Paciente(
                                cada_persona["nombre"],
                                cada_persona["edad"],
                                cada_persona["enfermedad"],
                                None,
                            )
                            hospital.añadir_paciente(nuevo_paciente)

                    # SEGUNDA PASADA: asignar los médicos a los pacientes
                    buscador_medicos = {}
                    for cada_persona_objeto in hospital.lista_personas:
                        if isinstance (cada_persona_objeto, Medico):
                            buscador_medicos[cada_persona_objeto.nombre] = cada_persona_objeto
                    
                    for cada_persona in cada_diccionario["Personas"]:
                        if cada_persona["Tipo"] == "Paciente" and cada_persona.get("medico_asignado"):
                            nombre_medico = cada_persona["medico_asignado"]
                            # Buscamos al paciente
                            for cada_objeto_paciente in hospital.lista_personas:
                                if cada_objeto_paciente.nombre == cada_persona["nombre"]:
                                    objeto_medico = buscador_medicos.get(nombre_medico)
                                    if objeto_medico:
                                        cada_objeto_paciente.asignar_medico(objeto_medico)
                                    break
                            
                    lista_de_hospitales.append(hospital)
                print("\nDatos cargados exitosamente")
            else:
                print("\nDatos corruptos. Se creará una nueva base de datos\n")
                return []       
        return lista_de_hospitales

    except FileNotFoundError:
        print("\nNo existen datos previos. Se creará una nueva base de datos")
        return []
    except json.JSONDecodeError:
        print("\nDatos corruptos. Se creará una nueva base de datos\n")
        return []


def validar_nombre(mensaje):
    while True:
        nombre = pedir_texto(mensaje)
        if len(nombre) < 3 or any(c.isdigit() for c in nombre):
            print(
                "\nEl nombre debe tener más de 3 caracteres, y contener únicamente letras."
            )
            continue
        return nombre


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


def introducir_nombre_hospital(lista, mensaje):
    while True:
        nombre = pedir_texto(mensaje)
        if nombre in ("S", "s"):
            return nombre, False
        tiene_numeros = any(c.isdigit() for c in nombre)
        if len(nombre) < 3 or tiene_numeros:
            print(
                "\nEl elemento introducido debe ser mayor a 3 caracteres, y contener únicamente letras."
            )
            continue
        if any(hospital.nombre == nombre for hospital in lista):
            print("\nYa registrado previamente")
            continue
        else:
            return nombre, True


def case1(nombre_del_hospital, lista_de_hospitales):
    objeto_hospital = Hospital(nombre_del_hospital)
    lista_de_hospitales.append(objeto_hospital)
    print("\nDatos guardados")


def case3_mostrar_relacion_de_medicos(hospital_actual: Hospital):
    lista_de_medicos = hospital_actual.extraer_medicos_de_lista_personas()
    if not lista_de_medicos:
        print("\nDebe contratar al menos un médico primero")
        return
    else:
        hospital_actual.lista_de_medicos()
    


def case2_if_lista_de_hospitales(lista_de_hospitales):
    menu_hospitales(lista_de_hospitales)
    opcion2 = escoer_opcion("\nOpción: ", range(1, len(lista_de_hospitales) + 2))
    if opcion2 == len(lista_de_hospitales) + 1:
        print("\nVolviendo al menú principal")
        time.sleep(1)
        return
    else:
        hospital_actual: Hospital = lista_de_hospitales[opcion2 - 1]
        print(f"\nBienvenidos al hospital {hospital_actual.nombre}")
        return hospital_actual


def contratar_medico(lista_de_hospitales, hospital_actual: Hospital):
    nombre_del_medico = hospital_actual.validar_medico()
    edad = pedir_edad("Edad: ")
    especialidad = validar_especialidad_medica(nombre_del_medico)
    medico1 = Medico(nombre_del_medico, edad, especialidad)
    hospital_actual.añadir_medico(medico1)
    guardar_datos(lista_de_hospitales)


def ingresar_paciente(hospital_actual: Hospital, lista_de_hospitales):
    nombre_del_paciente = hospital_actual.validar_paciente()
    edad = pedir_edad(f"Introducir edad de {nombre_del_paciente}: ")
    enfermedad = pedir_texto(
        f"Introduzca el motivo de consulta de {nombre_del_paciente}: "
    )
    print(f"\nSeleccione un médico para asignarle al paciente {nombre_del_paciente}")
    hospital_actual.lista_de_medicos() #imprime lista de medicos ordenados por especialidad
    lista_de_medicos = hospital_actual.extraer_medicos_de_lista_personas()
    lista_de_medicos.sort(key=lambda x: x.especialidad)
    if not lista_de_medicos:
        return
    
    opcion = escoer_opcion(
        "\nOpción: ",
        range(1, len(lista_de_medicos) + 1),
    )
    medico_asignado = lista_de_medicos[opcion - 1]
    print(
        f"\nHa seleccionado al médico {medico_asignado.nombre}, {medico_asignado.especialidad} para atender al paciente {nombre_del_paciente}."
    )
    paciente = Paciente(
        nombre_del_paciente,
        edad,
        enfermedad,
        medico_asignado,
    )
    hospital_actual.añadir_paciente(paciente)
    guardar_datos(lista_de_hospitales)


def mostrar_resumen(hospital_actual: Hospital):
    if len(hospital_actual.lista_personas) > 0:
        hospital_actual.mostrar_resumen()
    else:
        print("\nNo se ha guardado ningún dato todavía")


def case2(hospital_actual: Hospital, lista_de_hospitales):
    lista_medicos = hospital_actual.extraer_medicos_de_lista_personas()
    if not lista_medicos:
        print("\nDebe contratar al menos un médico primero")
        return
    else:
        ingresar_paciente(hospital_actual, lista_de_hospitales)


def mostrar_relacion_de_pacientes(hospital_actual: Hospital):
    lista_de_pacientes = hospital_actual.extraer_pacientes_de_lista_personas()
    if len(lista_de_pacientes) > 0:
        hospital_actual.lista_de_pacientes()
    else:
        print("\nNo se ha internado ningún paciente aún")


def case1_menu_inicial(lista_de_hospitales: list[Hospital]):
    nombre_del_hospital, bandera = introducir_nombre_hospital(
        lista_de_hospitales,
        "\nAñadir institución hospitalaria o presione 'S' para salir: ",
    )
    if bandera:
        case1(nombre_del_hospital, lista_de_hospitales)
        guardar_datos(lista_de_hospitales)


programa = True
print("\nSistema de gestión de pacientes")
lista_de_hospitales = descargar_datos()
try:
    while programa:
        menu_inicial()
        opcion1 = escoer_opcion("\nOpción: ", [1, 2, 3, 4])
        match opcion1:
            case 1:
                case1_menu_inicial(lista_de_hospitales)
            case 2:
                if lista_de_hospitales:
                    hospital_actual = case2_if_lista_de_hospitales(lista_de_hospitales)
                    if hospital_actual:
                        while True:
                            menu()
                            opcion = escoer_opcion("\nOpción: ", [1, 2, 3, 4, 5, 6, 7])
                            match opcion:
                                case 1:
                                    contratar_medico(
                                        lista_de_hospitales, hospital_actual
                                    )
                                case 2:
                                    case2(hospital_actual, lista_de_hospitales)
                                case 3:
                                    case3_mostrar_relacion_de_medicos(hospital_actual)
                                case 4:
                                    mostrar_relacion_de_pacientes(hospital_actual)
                                case 5:
                                    mostrar_resumen(hospital_actual)
                                case 6:
                                    break
                                case 7:
                                    programa = False
                                    break
                else:
                    print("\nNo se ha añadido ningún centro médico. Añada uno primero.")
            case 3:
                try:
                    if lista_de_hospitales:
                        exportar_datos(lista_de_hospitales)
                    else:
                        print(
                            "\nNo se ha añadido ningún centro médico. Añada uno primero."
                        )
                except PermissionError:
                    print(
                        "\nNo es posible guardar porque otra aplicación tiene abierto el programa. Ciérrelo e intente de nuevo."
                    )
            case 4:
                break

except KeyboardInterrupt:
    print("\n\n[!] Programa interrumpido por el usuario (Ctrl+C).")
    print("Guardando datos...")
    guardar_datos(lista_de_hospitales)
    print("Datos guardados")


except Exception as e:  # capturar errores inesperados  # noqa: BLE001
    print(f"\n[!] Ocurrió un error inesperado: {e}")
    print("Guardando datos...")
    guardar_datos(lista_de_hospitales)
    print("Datos guardados")

print("\nHa salido satisfactoriamente del programa.\n")

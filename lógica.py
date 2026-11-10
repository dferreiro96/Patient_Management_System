import time

from clases import *
from menus import menu_hospitales
from persistencia import guardar_datos
from utilidades import *


def validar_especialidad_medica(nombre_del_medico):
    especialidad = validar_nombre(f"Introducir especialidad de {nombre_del_medico}: ")
    return especialidad




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
    hospital_actual.lista_de_medicos()  # imprime lista de medicos ordenados por especialidad
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

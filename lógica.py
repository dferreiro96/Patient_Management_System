import time

from clases import Hospital, Medico, Paciente
from menus import menu_hospitales
from persistencia import guardar_datos
from utilidades import escoer_opcion, pedir_edad, pedir_texto, validar_nombre


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


def case1(lista_de_hospitales, nombre_del_hospital):
    lista_de_hospitales.append(Hospital(nombre_del_hospital))
    print("\nDatos guardados")
    

def case2(hospital_actual, lista_de_hospitales):
    if not hospital_actual:
        return
    if len(hospital_actual.lista_medicos) == 0:
        print("\nNo hay médicos en este hospital. Contrate uno primero")
    else:
        ingresar_paciente(lista_de_hospitales, hospital_actual)

def case3_mostrar_relacion_de_medicos(hospital_actual):
    if len(hospital_actual.lista_medicos) > 0:
        hospital_actual.lista_de_medicos()
    else:
        print("\nNo se ha contratado ningún médico aún")


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


def contratar_medico(lista_de_hospitales, hospital_actual):
    nombre_del_medico = hospital_actual.validar_medico()
    especialidad = validar_especialidad_medica(nombre_del_medico)
    medico1 = Medico(nombre_del_medico, especialidad)
    hospital_actual.añadir_medico(medico1)
    guardar_datos(lista_de_hospitales)


def ingresar_paciente(lista_de_hospitales, hospital_actual: Hospital):
    nombre_del_paciente = hospital_actual.validar_paciente()
    edad = pedir_edad(f"Introducir edad de {nombre_del_paciente}: ")
    enfermedad = pedir_texto(
        f"Introduzca el motivo de consulta de {nombre_del_paciente}: "
    )
    print(f"\nSeleccione un médico para asignarle al paciente {nombre_del_paciente}")
    hospital_actual.seleccionar_medico()

    opcion = escoer_opcion(
        "\nOpción: ",
        range(1, len(hospital_actual.lista_medicos) + 1),
    )
    medico_asignado = hospital_actual.lista_medicos[opcion - 1]
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


def case1_menu_inicial(lista_de_hospitales):
    nombre_del_hospital, bandera = introducir_nombre_hospital(lista_de_hospitales, "\nAñadir institución hospitalaria o presione 'S' para salir: ")
    if bandera:
        case1(nombre_del_hospital, lista_de_hospitales)
        guardar_datos(lista_de_hospitales)

                    
def mostrar_resumen(hospital_actual):
    if (
        len(hospital_actual.lista_pacientes) > 0
        or len(hospital_actual.lista_medicos) > 0
    ):
        hospital_actual.mostrar_resumen()
    else:
        print("\nNo se ha guardado ningún dato todavía")


def mostrar_relacion_de_pacientes(hospital_actual):
    if len(hospital_actual.lista_pacientes) > 0:
        hospital_actual.lista_de_pacientes()
    else:
        print("\nNo se ha internado ningún paciente aún")

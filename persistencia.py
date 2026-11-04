import csv
import json

from clases import Hospital, Medico, Paciente
from utilidades import convertir_a_diccionario


def guardar_datos(lista_de_hospitales):
    datos = convertir_a_diccionario(lista_de_hospitales)
    with open("Datos_hospital.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


def exportar_datos(lista_de_hospitales):
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
            for medico in hospital.lista_medicos:
                escritor.writerow(
                    {
                        "Hospital": hospital.nombre,
                        "Clase": "Médico",
                        "Nombre": medico.nombre,
                        "Edad": "-",
                        "Especialidad/Afección": medico.especialidad,
                        "Médico Asignado": "-",
                    }
                )
            for paciente in hospital.lista_pacientes:
                escritor.writerow(
                    {
                        "Hospital": hospital.nombre,
                        "Clase": "Paciente",
                        "Nombre": paciente.nombre,
                        "Edad": paciente.edad,
                        "Especialidad/Afección": paciente.enfermedad,
                        "Médico Asignado": paciente.medico_asignado.nombre
                        if paciente.medico_asignado
                        else "Ninguno",
                    }
                )
        print(
            f"\nSe han exportado los datos correctamente al archivo llamado: {nombre_del_archivo}"
        )


def cargar_datos():
    try:
        with open("Datos_hospital.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            lista_de_hospitales = []
            for diccionario_hospitales in datos:
                hospital = Hospital(diccionario_hospitales["Nombre"])

                # reconstruyendo medicos

                for diccionario_de_medicos in diccionario_hospitales["Médicos"]:
                    medico = diccionario_de_medicos["Nombre"]
                    especialidad = diccionario_de_medicos["Especialidad"]
                    nuevo_medico = Medico(medico, especialidad)
                    hospital.lista_medicos.append(nuevo_medico)

                # reconstruyendo pacientes

                for diccionario_de_pacientes in diccionario_hospitales["Pacientes"]:
                    medico_asignado = None
                    if diccionario_de_pacientes["Médico asignado"]:
                        for med in hospital.lista_medicos:
                            if (
                                med.nombre
                                == diccionario_de_pacientes["Médico asignado"]
                            ):
                                medico_asignado = med
                                break
                    nombre = diccionario_de_pacientes["Nombre"]
                    edad = diccionario_de_pacientes["Edad"]
                    enfermedad = diccionario_de_pacientes["Afección"]
                    nuevo_paciente = Paciente(nombre, edad, enfermedad, medico_asignado)
                    hospital.lista_pacientes.append(nuevo_paciente)
                lista_de_hospitales.append(hospital)
        print("\nDatos cargados exitosamente")
        return lista_de_hospitales
    except FileNotFoundError:
        print("\nNo existen datos previos. Se creará una nueva base de datos")
        return []
    except json.JSONDecodeError:
        print("\nDatos corruptos. Se creará una nueva base de datos\n")
        return []

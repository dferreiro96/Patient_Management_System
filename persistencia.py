import csv
import json

from clases import Hospital, Medico, Paciente


def guardar_datos(lista_de_hospitales):
    datos = convertir_a_diccionario(lista_de_hospitales)
    with open("Datos_hospital.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

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
                if isinstance(persona, Medico):
                    especialidad_afeccion = persona.especialidad
                    medico_asignado = "-"
                else:
                    especialidad_afeccion = persona.enfermedad
                    medico_asignado = (
                        persona.medico_asignado.nombre
                        if persona.medico_asignado
                        else "Ninguno"
                    )

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

                    for cada_persona in cada_diccionario[
                        "Personas"
                    ]:  # reconstruyendo medicos
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
                        if isinstance(cada_persona_objeto, Medico):
                            buscador_medicos[cada_persona_objeto.nombre] = (
                                cada_persona_objeto
                            )

                    for cada_persona in cada_diccionario["Personas"]:
                        if cada_persona["Tipo"] == "Paciente" and cada_persona.get(
                            "medico_asignado"
                        ):
                            nombre_medico = cada_persona["medico_asignado"]
                            # Buscamos al paciente
                            for cada_objeto_paciente in hospital.lista_personas:
                                if (
                                    cada_objeto_paciente.nombre
                                    == cada_persona["nombre"]
                                ):
                                    objeto_medico = buscador_medicos.get(nombre_medico)
                                    if objeto_medico:
                                        cada_objeto_paciente.asignar_medico(
                                            objeto_medico
                                        )
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

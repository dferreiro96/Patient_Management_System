from utilidades import validar_nombre


class Medico:
    def __init__(self, nombre, especialidad=None):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Dr(a). {self.nombre} ({self.especialidad})"

    def mostrar_medico(self):
        print(f"Dr. {self.nombre} - {self.especialidad}")


class Paciente:
    def __init__(self, nombre, edad, enfermedad, medico_asignado):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad
        self.medico_asignado = medico_asignado

    def __str__(self):
        return f"{self.nombre}"

    def asignar_medico(self, medico):
        self.medico_asignado = medico

    def mostrar_paciente(self):
        if self.medico_asignado:
            print(
                f"\nPaciente: {self.nombre}, {self.edad} años. Afección: {self.enfermedad} - Médico asignado: {self.medico_asignado}"
            )
        else:
            print(f"\nPaciente: {self.nombre} - No tiene médico asignado")


class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_medicos = []
        self.lista_pacientes = []

    def validar_medico(self):
        while True:
            nombre = validar_nombre("\nIntroduzca el nombre del médico: ")
            if any(m.nombre == nombre for m in self.lista_medicos):
                print("\nYa registrado previamente")
            else:
                return nombre

    def añadir_medico(self, nuevo_medico):
        self.lista_medicos.append(nuevo_medico)
        print(f"\nSe ha contratado al {nuevo_medico}")

    def añadir_paciente(self, nuevo_paciente):
        self.lista_pacientes.append(nuevo_paciente)
        print(
            f"\nSe ha ingresado al paciente {nuevo_paciente}, {nuevo_paciente.edad} años, que acudió por: {nuevo_paciente.enfermedad}; y será atendido por {nuevo_paciente.medico_asignado}"
        )

    def validar_paciente(self):
        while True:
            nombre = validar_nombre("\nIntroduzca el nombre del paciente: ")
            if any(m.nombre == nombre for m in self.lista_pacientes):
                print("\nYa registrado previamente")
            else:
                return nombre

    def lista_de_medicos(self):
        print("\n_____RESUMEN______")
        print(f"\nHOSPITAL {self.nombre}\n")
        print("Lista de médicos contratados\n")
        self.lista_medicos.sort(key=lambda x: x.especialidad)
        for i, med in enumerate(self.lista_medicos, start=1):
            print(f"{i}. Nombre: {med.nombre} --- Especialidad: {med.especialidad}")

    def lista_de_pacientes(self):
        print("\n_____RESUMEN______")
        print(f"\nHOSPITAL {self.nombre}\n")
        print("Lista de pacientes ingresados\n")
        ordenados = sorted(self.lista_pacientes, key=lambda x: x.nombre)
        for i, pac in enumerate(ordenados, start=1):
            print(
                f"{i}. Nombre: {pac.nombre} - Edad: {pac.edad} años - Motivo de consulta: {pac.enfermedad} - Médico asignado: {pac.medico_asignado}"
            )

    def seleccionar_medico(self):
        print("\nLista de médicos contratados\n")
        self.lista_medicos.sort(key=lambda x: x.especialidad)
        for i, med in enumerate(self.lista_medicos, start=1):
            print(f"{i}. Nombre: {med.nombre} --- Especialidad: {med.especialidad}")

    def mostrar_resumen(self):
        print("\n_____RESUMEN______")
        print(f"\nHOSPITAL {self.nombre}\n")
        print("Lista de médicos contratados")
        print("__________________________\n")
        if self.lista_medicos:
            ordenados = sorted(self.lista_medicos, key=lambda x: x.nombre)
            for i, med in enumerate(ordenados, start=1):
                print(f"{i}. Nombre: {med.nombre}---Especialidad: {med.especialidad}")
            print(f"\nTotal de médicos contratados: {len(self.lista_medicos)}")
            print()
        else:
            print("\nNo se han contratado médicos todavía\n")
        print("\nLista de pacientes")
        print("____________________")
        if self.lista_pacientes:
            self.lista_pacientes.sort(key=lambda x: x.nombre)
            for i, pac in enumerate(self.lista_pacientes, start=1):
                print(f"{i}. Nombre: {pac.nombre}")
            print(f"\nTotal de pacientes ingresados: {len(self.lista_pacientes)}")
        else:
            print("\nNo se han ingresado pacientes todavía\n")

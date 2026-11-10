from utilidades import validar_nombre


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

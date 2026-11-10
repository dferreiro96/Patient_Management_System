# Hospital Management System 🏥

## 🇬🇧 English

A comprehensive command-line hospital management application built in Python. It allows users to manage multiple hospitals, hiring doctors, admitting patients, and assigning doctors to patients. The system features robust data persistence, global reporting, and a clean, modular Object-Oriented design.

### Features

- 🏢 **Multi-Hospital Support:** Create and manage multiple medical institutions, each with its own independent lists of doctors and patients.
- 👨‍⚕️ **Doctor Management:** Hire doctors, assign specialties, and prevent duplicate registrations.
- 🤒 **Patient Admission:** Admit patients, record their age and ailment, and assign an available doctor.
- 🛡️ **Input Validation:** Robust handling of invalid inputs (names, ages, menu options) to prevent crashes.
- 💾 **Automatic Persistence:** Automatically saves the entire system state (hospitals, doctors, patients) to a JSON file after every action, ensuring no data is lost.
- 📊 **CSV Export:** Generate a comprehensive global report in CSV format, ready to be analyzed in Excel.
- 🛑 **Crash Protection:** Uses `try/except` blocks (including `KeyboardInterrupt` and `PermissionError`) to save data and exit gracefully even if the program is interrupted or a file is locked.
- **Object-Oriented Design:** Uses inheritance (`Persona`, `Medico`, `Paciente`) and polymorphism for clean, scalable code.

### Requirements

- Python 3.10 or higher (uses `match` statements and modern type hinting).
- No external dependencies — only the standard library (`json`, `csv`, `time`).

### Usage

1. Clone or download the project files.
2. Ensure you run the main script from the root folder:
 main.py

### Project Structure

The code is fully modularized to separate concerns (UI, Logic, and Data):
<img width="773" height="369" alt="estructuta_ingles" src="https://github.com/user-attachments/assets/8dd85f85-27a8-4c0a-8611-ff57ff26807d" />

### Data Storage

The system automatically saves data to Datos_hospital.json after modifying the state. If the file is missing or corrupted, the system starts with an empty state.

Example JSON structure:

<img width="539" height="412" alt="Almacenamiento de datos" src="https://github.com/user-attachments/assets/98da439d-a411-4eaa-813f-739f5af2bcfa" />

### Possible Improvements

- Migration from JSON to a relational database (like SQLite) for better performance with large datasets.

- Add a Graphical User Interface (GUI) using tkinter or customtkinter.




## 🇪🇸 Español

Una completa aplicación de consola para la gestión hospitalaria construida en Python. Permite gestionar múltiples hospitales, contratar médicos, ingresar pacientes y asignar médicos a cada uno. El sistema cuenta con persistencia de datos robusta, reportes globales y un diseño limpio y modular orientado a objetos.

### Características 

- 🏢 Soporte Multi-Hospital: Crea y gestiona múltiples instituciones médicas, cada una con sus propias listas independientes de médicos y pacientes.

- 👨‍⚕️ Gestión de Médicos: Contrata médicos, asigna especialidades y evita registros duplicados.

- 🤒 Ingreso de Pacientes: Ingresa pacientes, registra su edad y motivo de consulta, y asígnales un médico disponible.

- 🛡️ Validación de Entradas: Manejo robusto de entradas inválidas (nombres, edades, opciones del menú) para evitar que el programa falle.

- 💾 Persistencia Automática: Guarda automáticamente todo el estado del sistema (hospitales, médicos, pacientes) en un archivo JSON después de cada acción, evitando la pérdida de datos.

- 📊 Exportación a CSV: Genera un reporte global en formato CSV, listo para ser analizado en Excel.

- 🛑 Protección contra Cierres: Utiliza bloques try/except (incluyendo KeyboardInterrupt y PermissionError) para guardar datos y salir elegantemente si el programa se interrumpe o un archivo está bloqueado.

- **Diseño Orientado a Objetos:** Usa herencia (`Persona`, `Medico`, `Paciente`) y polimorfismo para un código limpio y escalable.

### Requisitos

- Python 3.10 o superior (usa match y anotaciones de tipo modernas).
- Sin dependencias externas — solo la librería estándar (json, csv, time).

### Uso
Clona o descarga los archivos del proyecto.

Ejecuta el script principal:
- main.py
- Navega a través de los menús interactivos.

### Estructura del proyecto

El código está completamente modularizado para separar responsabilidades (Interfaz, Lógica y Datos):

<img width="761" height="447" alt="Estructura Español" src="https://github.com/user-attachments/assets/04970d8a-b2bd-4915-b363-cf1781a57ad3" />


### Mejoras posibles

- Migrar de JSON a una base de datos relacional (como SQLite) para un mejor rendimiento con grandes volúmenes de datos.

- Añadir una Interfaz Gráfica de Usuario (GUI) usando tkinter o customtkinter.


### 📄 License / Licencia

Free to use and modify for personal or educational purposes.
Libre para usar y modificar con fines personales o educativos.

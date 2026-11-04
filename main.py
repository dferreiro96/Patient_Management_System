
from lógica import (
    case1_menu_inicial,
    case2,
    case2_if_lista_de_hospitales,
    case3_mostrar_relacion_de_medicos,
    contratar_medico,
    mostrar_relacion_de_pacientes,
    mostrar_resumen,
)
from menus import menu, menu_inicial
from persistencia import cargar_datos, exportar_datos, guardar_datos
from utilidades import escoer_opcion


def main():
    programa = True

    print("\nSistema de gestión de pacientes")
    lista_de_hospitales = cargar_datos()
    try:
        while programa:
            menu_inicial()
            opcion1 = escoer_opcion("\nOpción: ", [1, 2, 3, 4])
            match opcion1:
                case 1:
                    case1_menu_inicial(lista_de_hospitales)
                case 2:
                    if lista_de_hospitales:
                        hospital_actual = case2_if_lista_de_hospitales(
                            lista_de_hospitales
                        )
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
                        exportar_datos(lista_de_hospitales)
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


if __name__ == "__main__":
    main()

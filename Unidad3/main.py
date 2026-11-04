from computadoras import *
from reportes import *

# MENÚ PRINCIPAL

opcion = 0
while opcion <= 9:
    print("\n==========================")
    print("    SISTEMA DE PRESTAMOS    ")
    print("\n==========================")
    print("1. Consultar computadoras")
    print("2. Buscar por software")
    print("3. Solicitar prestamo")
    print("4. Devolver computadora")
    print("5. Crear reservación")
    print("6. Agregar computadora")
    print("7. Historial de Prestamos")
    print("8. Historial de Necesidades")
    print("9. Estadisticas")
    print("10. Salir")
    print("\n==========================")
    
    opcion = int(input("Seleccione una opción: "))

    # 1. Consultar computadora
    if opcion == 1:
        listar_computadoras()

    # 2. Buscar por software
    elif opcion == 2:
        buscar_sw()

    # 3. Solicitar préstamo
    elif opcion == 3:
        solicitar_prestamo()

    # 4. Devolver computadora
    elif opcion == 4:
        devolver_computadora()


    # 6. Agregar computadora
    elif opcion == 6:
        agregar_computadora()

    # 7. Historial de prestamos
    elif opcion == 7:
        historial_prestamos()

    # 8. Historial de necesidades
    elif opcion == 8:
        historial_necesidades()

    # 9. Estadisticas
    elif opcion == 9:
        estadisticas()

    # 10. Salir
    elif opcion == 10:
        print("\nGracias por utilizar el sistema.")

    else:
        print("\nOpción no válida.")
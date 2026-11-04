from datos import *

#7
def historial_prestamos():
    print("\n--- HISTORIAL DE PRESTAMOS DE COMPUTADORAS ---")
    cantidad_prestamos = len(prestamos)
    if cantidad_prestamos > 0:
        for i in range(len(prestamos)):
            print(i+1, " | Num_control:", prestamos[i]["num_control"],
                  "| Software:", prestamos[i]["programa"],
                  " | Aula:", prestamos[i]["aula"],
                  "| ID:", prestamos[i]["id"] )
    else:
        print("No se han registrado prestamos")

#8
def historial_necesidades():
    print("\n\n=================================")
    print("Historico de necesidades")
    for i in range(len(necesidades)):
        print("Programa:", necesidades[i]["programa"], "| Fecha:", necesidades[i]["fecha"])

#9
def estadisticas():
    # Diccionario para contar préstamos por carrera
    conteo_carreras = {}
    for prestamo in prestamos:
        carrera = "Carrera no encontrada"
        for alumno in alumnos:
            if alumno["num_control"] == prestamo["num_control"]:
                carrera = alumno["carrera"]
                break
        if carrera in conteo_carreras:
            conteo_carreras[carrera] += 1
        else:
            conteo_carreras[carrera] = 1

    print("\n==============================")
    print("Estadísticas por carrera:")
    if conteo_carreras:
        for carrera, cantidad in conteo_carreras.items():
            print(carrera, ":", cantidad, "veces")
    else:
        print("No hay préstamos registrados.")

    # Diccionario para contar préstamos por software solicitado
    conteo_programas = {}
    for prestamo in prestamos:
        programa = prestamo["programa"].lower()
        
        if programa in conteo_programas:
            conteo_programas[programa] += 1
        else:
            conteo_programas[programa] = 1

    print("\nEstadísticas por programa:")
    if conteo_programas:
        for programa, cantidad in conteo_programas.items():
            print(programa, ":", cantidad, "veces")
    else:
        print("No hay préstamos registrados.")
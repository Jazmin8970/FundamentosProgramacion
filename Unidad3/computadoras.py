from datos import *
import datetime

# 1. Consultar computadoras
def listar_computadoras():
    print("\n--- COMPUTADORAS ---")
    for pc in computadoras:
        print("Aula:", pc["aula"], "| ID:", pc["id"], "| Software:", pc["programas"], "| Estado:", pc["estado"])


# 2. Buscar por software
def buscar_sw():
    programa = input("\nIngrese el software que desea buscar: ")
    print("\n--- RESULTADOS ---")
    encontrado = False
    for pc in computadoras:
        if programa.lower() in pc["programas"].lower():
            print("ID:", pc["id"], 
                  "| Aula:", pc["aula"],
                  "| Software:", pc["programas"],
                  "| Estado:", pc["estado"])
            encontrado = True

    if not encontrado:
        print("No se encontraron computadoras con ese software.")


# 3. Solicitar préstamo
def solicitar_prestamo():
    print("\n--- SOLICITAR PRÉSTAMO ---")
    num_control = input("Ingrese el número de control: ")

    # Verificar si el alumno existe
    existe_alumno = False
    for alu in alumnos:
        if str(alu["num_control"]) == num_control:
            existe_alumno = True
            break

    if existe_alumno:
        programa = input("¿Qué programa necesita?: ")

        pc_encontrada = None
        # Buscar computadora que tenga el programa
        for pc in computadoras:
            if programa.lower() in pc["programas"].lower():
                pc_encontrada = pc
                if pc["estado"] == "Disponible":
                    pc["estado"] = "Prestada"
                    print(f"Se asignó la computadora {pc['id']} que está en el aula {pc['aula']}")
                    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    prestamos.append({
                        "num_control": num_control,
                        "programa": programa,
                        "aula": pc["aula"],
                        "id": pc["id"],
                        "fecha": fecha_actual
                    })
                    return
                
        # Si encontró el programa pero no estaba disponible
        if pc_encontrada is not None:
            print(f"Sí se encontró el software, pero la computadora está {pc_encontrada['estado']}.")
        else:
            # Si el programa NO existe en ninguna computadora
            resp = input("El programa no existe. ¿Desea agregarlo a necesidades? (s/n): ")
            if resp.lower() == 's':
                fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                necesidades.append({"programa": programa, "fecha": fecha})
                print("Agregado a la lista de necesidades.")
    else:
        print("El alumno no existe.")

# 4. Devolver computadora
def devolver_computadora():
    print("\n--- DEVOLVER COMPUTADORA ---")
    id_pc = input("Dame el ID de la computadora: ")
    existe = False

    for pc in computadoras:
        if str(pc["id"]) == id_pc:
            existe = True
            if pc["estado"] in ["Prestada", "Reservada"]:
                pc["estado"] = "Disponible"
                print(f"La computadora {id_pc} ya está disponible.")
            else:
                print(f"La computadora {id_pc} no está prestada/reservada (Estado actual: {pc['estado']}).")
            break

    if not existe:
        print(f"La computadora {id_pc} no existe.")


# 6. Agregar computadora
def agregar_computadora():
    print("\n--- AGREGAR COMPUTADORA ---")
    id_computadora = input("ID de la computadora: ")
    aula = input("Aula: ")
    programas = input("Software instalado: ")
    
    nueva_compu = {
        "id": id_computadora,
        "aula": aula,
        "programas": programas,
        "estado": "Disponible"
    }
    computadoras.append(nueva_compu)
    print("\nComputadora agregada correctamente.")
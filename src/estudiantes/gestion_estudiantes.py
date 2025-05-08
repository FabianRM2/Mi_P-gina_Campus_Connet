estudiantes = []

def agregar_estudiante(nombre, apellido, id_estudiante):
    estudiante = Estudiante(nombre, apellido, id_estudiante)
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} {apellido} agregado.")

def listar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes:")
        for estudiante in estudiantes:
            estudiante.mostrar_info()

# Aquí puedes agregar más funciones (buscar, eliminar, etc.)
from estudiante import Estudiante

estudiantes = []

def agregar_estudiante(nombre, apellido, id_estudiante):
    estudiante = Estudiante(nombre, apellido, id_estudiante)
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} {apellido} agregado.")

def listar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes:")
        for estudiante in estudiantes:
            estudiante.mostrar_info()

def buscar_estudiante(id_estudiante):
    for estudiante in estudiantes:
        if estudiante.id_estudiante == id_estudiante:
            return estudiante
    return None

# Código de prueba (puedes descomentarlo para probar la función buscar_estudiante)
# if __name__ == "__main__":
#     agregar_estudiante("Ana", "Pérez", "1001")
#     agregar_estudiante("Carlos", "López", "1002")
#
#     estudiante_encontrado = buscar_estudiante("1002")
#     if estudiante_encontrado:
#         print("\nEstudiante encontrado:")
#         estudiante_encontrado.mostrar_info()
#     else:
#         print("\nNo se encontró el estudiante.")
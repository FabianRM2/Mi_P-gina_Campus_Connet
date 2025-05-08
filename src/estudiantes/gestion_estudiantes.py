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
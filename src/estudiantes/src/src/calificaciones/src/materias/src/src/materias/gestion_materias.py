from materia import Materia

materias = []

def agregar_materia(codigo_materia, nombre_materia, id_profesor_asignado=None, creditos=None):
    materia = Materia(codigo_materia, nombre_materia, id_profesor_asignado, creditos)
    materias.append(materia)
    print(f"Materia {nombre_materia} con código {codigo_materia} agregada.")

def obtener_materia_por_codigo(codigo_materia):
    for materia in materias:
        if materia.codigo_materia == codigo_materia:
            return materia
    return None

def asignar_profesor_a_materia(codigo_materia, id_profesor):
    materia = obtener_materia_por_codigo(codigo_materia)
    if materia:
        materia.id_profesor_asignado = id_profesor
        print(f"Profesor {id_profesor} asignado a la materia {codigo_materia}.")
    else:
        print(f"No se encontró la materia con código {codigo_materia}.")

def listar_todas_materias():
    if not materias:
        print("No hay materias registradas.")
    else:
        print("Lista de materias:")
        for materia in materias:
            materia.mostrar_info()

def eliminar_materia(codigo_materia):
    global materias
    materias = [materia for materia in materias if materia.codigo_materia != codigo_materia]
    print(f"Materia con código {codigo_materia} eliminada.")

# Ejemplo de uso (puedes descomentarlo para probar)
# if __name__ == "__main__":
#     agregar_materia("MAT001", "Matemáticas I", creditos=4)
#     agregar_materia("FIS001", "Física General", creditos=3)
#
#     listar_todas_materias()
#
#     asignar_profesor_a_materia("MAT001", "PROF001")
#
#     materia_encontrada = obtener_materia_por_codigo("FIS001")
#     if materia_encontrada:
#         print("\nMateria encontrada:")
#         materia_encontrada.mostrar_info()
#
#     eliminar_materia("FIS001")
#     listar_todas_materias()
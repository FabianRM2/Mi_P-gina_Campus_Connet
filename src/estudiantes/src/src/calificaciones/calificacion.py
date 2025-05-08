class Calificacion:
    def __init__(self, id_calificacion, id_estudiante, codigo_materia, valor, fecha_registro=None):
        self.id_calificacion = id_calificacion  # Clave primaria
        self.id_estudiante = id_estudiante  # Clave foránea referenciando a ESTUDIANTE
        self.codigo_materia = codigo_materia  # Clave foránea referenciando a MATERIA
        self.valor = valor
        self.fecha_registro = fecha_registro

    def mostrar_info(self):
        info = f"ID Calificación: {self.id_calificacion}"
        info += f", ID Estudiante: {self.id_estudiante}"
        info += f", Código Materia: {self.codigo_materia}"
        info += f", Valor: {self.valor}"
        if self.fecha_registro:
            info += f", Fecha Registro: {self.fecha_registro}"
        print(info)


        from calificacion import Calificacion

calificaciones = []

def registrar_calificacion(id_calificacion, id_estudiante, codigo_materia, valor, tipo_evaluacion=None, observaciones=None, fecha_registro=None):
    calificacion = Calificacion(id_calificacion, id_estudiante, codigo_materia, valor, tipo_evaluacion, observaciones, fecha_registro)
    calificaciones.append(calificacion)
    print(f"Calificación registrada con ID: {id_calificacion}")

def obtener_calificaciones_estudiante(id_estudiante):
    return [calificacion for calificacion in calificaciones if calificacion.id_estudiante == id_estudiante]

def obtener_calificaciones_materia(codigo_materia):
    return [calificacion for calificacion in calificaciones if calificacion.codigo_materia == codigo_materia]

def actualizar_calificacion(id_calificacion, nuevo_valor=None, nuevo_tipo_evaluacion=None, nuevas_observaciones=None):
    for calificacion in calificaciones:
        if calificacion.id_calificacion == id_calificacion:
            if nuevo_valor is not None:
                calificacion.valor = nuevo_valor
            if nuevo_tipo_evaluacion is not None:
                calificacion.tipo_evaluacion = nuevo_tipo_evaluacion
            if nuevas_observaciones is not None:
                calificacion.observaciones = nuevas_observaciones
            print(f"Calificación con ID {id_calificacion} actualizada.")
            return
    print(f"No se encontró calificación con ID {id_calificacion}.")

def eliminar_calificacion(id_calificacion):
    global calificaciones
    calificaciones = [calificacion for calificacion in calificaciones if calificacion.id_calificacion != id_calificacion]
    print(f"Calificación con ID {id_calificacion} eliminada.")

def listar_todas_calificaciones():
    if not calificaciones:
        print("No hay calificaciones registradas.")
    else:
        print("Lista de calificaciones:")
        for calificacion in calificaciones:
            calificacion.mostrar_info()

# Ejemplo de uso (puedes descomentarlo para probar)
# if __name__ == "__main__":
#     registrar_calificacion("CAL001", "1001", "MAT001", 4.5, "Parcial 1", "Buen desempeño")
#     registrar_calificacion("CAL002", "1001", "MAT001", 3.8, "Parcial 2")
#     registrar_calificacion("CAL003", "1002", "MAT001", 4.0, "Examen Final", "Necesita mejorar en el próximo")
#
#     print("\nCalificaciones del estudiante 1001:")
#     for calificacion in obtener_calificaciones_estudiante("1001"):
#         calificacion.mostrar_info()
#
#     print("\nCalificaciones de la materia MAT001:")
#     for calificacion in obtener_calificaciones_materia("MAT001"):
#         calificacion.mostrar_info()
#
#     actualizar_calificacion("CAL002", nuevo_valor=4.2, nuevas_observaciones="Mejoró")
#     listar_todas_calificaciones()
#
#     eliminar_calificacion("CAL003")
#     listar_todas_calificaciones()

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}, ID: {self.id_estudiante}")



# Aquí puedes agregar más funciones (buscar, eliminar, etc.)

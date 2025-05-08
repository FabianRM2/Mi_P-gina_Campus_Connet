class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}, ID: {self.id_estudiante}")



# Aquí puedes agregar más funciones (buscar, eliminar, etc.)
class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}, ID: {self.id_estudiante}")


        class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante, edad=None, grado=None, direccion=None, telefono=None, correo_personal=None, fecha_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.edad = edad
        self.grado = grado
        self.direccion = direccion
        self.telefono = telefono
        self.correo_personal = correo_personal
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info(self):
        info = f"Nombre: {self.nombre} {self.apellido}, ID: {self.id_estudiante}"
        if self.edad:
            info += f", Edad: {self.edad}"
        if self.grado:
            info += f", Grado: {self.grado}"
        if self.direccion:
            info += f", Dirección: {self.direccion}"
        if self.telefono:
            info += f", Teléfono: {self.telefono}"
        if self.correo_personal:
            info += f", Correo Personal: {self.correo_personal}"
        if self.fecha_nacimiento:
            info += f", Fecha de Nacimiento: {self.fecha_nacimiento}"
        print(info)
class Profesor:
    def __init__(self, nombre, apellido, id_profesor, correo_institucional, contraseña, materias_dicta=None):
        self.nombre = nombre
        self.apellido = apellido
        self.id_profesor = id_profesor
        self.correo_institucional = correo_institucional
        self.contraseña = contraseña  # ¡Importante! Esto nunca debe almacenarse en texto plano en una aplicación real.
        self.materias_dicta = materias_dicta if materias_dicta is not None else []

    def mostrar_info(self):
        info = f"Nombre: {self.nombre} {self.apellido}, ID Profesor: {self.id_profesor}"
        info += f", Correo Institucional: {self.correo_institucional}"
        if self.materias_dicta:
            info += f", Materias Dicta: {', '.join(self.materias_dicta)}"
        print(info)
        
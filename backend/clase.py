class Clase():
    nombre = ""
    profesor = ""
    alumnos = []
    precio = 0
    def __init__(self, nombre, profesor, precio):
        self.nombre = nombre
        self.profesor = profesor
        self.precio = precio

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
    def eliminar_alumno(self, alumno):
        self.alumnos.remove(alumno)

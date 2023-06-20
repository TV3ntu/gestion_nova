from datetime import datetime, timedelta
class Persona():
    """
    Clase que representa a una persona
    """
    nombre = ""
    apellido = ""
    direccion = ""
    telefono = ""
    fecha_nacimiento = ""
    clases = []
    def __init__(self, nombre, apellido, direccion, telefono, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
    def get_edad(self):
        """
        Calcula la edad de la persona
        :return:
        """
        return (datetime.today() - datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y")).days / 365


class Profesor(Persona):
    def sueldo_mensual(self):
        """
        Calcula el sueldo mensual del profesor
        :return:
        """
        total = 0
        for clase in self.clases:
            total += clase.precio * len(clase.alumnos) / 2
        return total
class Alumno(Persona):
    pagos = []
    def pago_mensual(self):
        """
        Calcula el pago mensual del alumno
        :return:
        """
        total = 0
        for clase in self.clases:
            total += clase.precio
        return total

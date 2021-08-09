class Alumno():
    def __init__(self,nombre,puntos):
        self.nombre = nombre
        self.puntos = puntos


    # metodo getter para nombre
    def get_nombre(self):
        return self.nombre

    #metodo setter para nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    # metodo getter para puntos
    def get_puntos(self):
        return self.puntos

    #metodo setter para puntos
    def set_puntos(self, puntos):
        self.puntos = puntos

    
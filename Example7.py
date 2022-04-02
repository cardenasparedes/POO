#Herencia múltiple: permite que una clase derivada herede de másde una clase o padre.

# class ClaseDerivada (ClaseA, ClaseB):
#   "contenido de la clase"

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Instituto:
    def presentarinstituto(self):
        print("Estudio en SENATI")
        
class InteligenciaArtificial(Estudiante, Instituto): #en el paréntesis indicamos las clases padres
    def presentarse(self):
        print("Hola soy",self.nombre, "tengo", self.edad, "años y estudio Inteligencia artificial en Ingenieria de Software.")
        
estudiante1 = InteligenciaArtificial("Jhon Doe", 20)
estudiante1.presentarse()
estudiante1.presentarinstituto()
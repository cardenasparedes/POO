# Escribir un programa en pyhon que verifique la edad de
# una persona si es mayor o menor de edad. 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comprobar_edad (self):
        if persona1.edad >= 18:
            print(persona1.nombre, "es mayor de edad.")
        else:
            print(persona1.nombre, "es menor de edad")

persona1 = Persona("Jhon doe", 50)
persona1.comprobar_edad()
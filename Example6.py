# #Herencia única: permite que una clase derivada herede características de una sola clase principal.

# class Empleado(): #este es el la clase padre
#     def __init__(self, nombre, edad, salario):
#         self.nombre = nombre 
#         self.edad = edad 
#         self.salario = salario
    
# class EmpleadoSupervisor(Empleado): # este es la clase hija de empleado
#     def  __init__(self, nombre, edad, salario,id):
#         self.nombre = nombre 
#         self.edad = edad 
#         self.salario = salario
#         self.id = id 
        
# empleado1= Empleado("Raul Sanchez", 22, 1000)

# print(empleado1.edad, "años")

class Estudiante: # creamos la clase padre
    def __init__(self, edad, nombre): #definimos los parámetros edad y nombre.
        self.edad = edad # declaramos el atributo edad es igual al argumento edad.
        self.nombre = nombre # declaramos el atributo nomrbe es igual al argumento nombre.

class IngenieriaSoftware(Estudiante): # en el paréntesis indicamos la clase padre o clase principal Estudiante.
    def presentarse(self): # creamos el método presentarse.
        print("Hola, mi nombre es",self.nombre, "tengo", self.edad, "años y me encuentro cursando la carrera de Ingenieria de Software.")
        
Jhon = IngenieriaSoftware(30, "Jhon Doe")
Jhon.presentarse()
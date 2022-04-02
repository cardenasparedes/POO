#Crear una clase con instancia de atributos

class Employee:
    #definiendo las propiedades y asignando valores
    id_employee = 5
    salario = 2000  
    departameno = "Recursos Humanos"
    horario= "Diurno"
    
#crear un objeto de la clase Employee 
Saul = Employee()

# imprimir las propiedades de Saul
print("id =", Saul.id_employee)
print("Salario de Saul =", Saul.salario)
print("El Area o departamento =", Saul.departameno)
print("El horario del trabajador es =", Saul.horario)
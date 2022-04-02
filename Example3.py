# Escribir un programa en python para crear una clase Vehicle con atributos de instancia. max_speed millage(max velocidad y kilometraje). 

from cgi import print_form


class Vehicle:
    def __init__(self, max_speed, millage):
        self.max_speed = max_speed
        self.millage = millage
        
modelotoyota = Vehicle(240, 20)

print("La velocidad del vehiculo toyota es : ", modelotoyota.max_speed)
print("El kilometraje recorrido por toyota es : {}".format(modelotoyota.millage))

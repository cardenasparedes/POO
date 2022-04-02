#Escribir un programa en pyhon para crear una clase Articulo con atributos de instancia: código del artículo, cantidad, precio.

#métodos: mostrar la cantidad actual, mostrar el precio, reducir la cantidad actual, incrementa la cantidad actual. 

#correo del profesor: ccamposco@senati.pe

class Articulo:
    def __init__(self, codigo, cantidad, precio): 
        self.cod = codigo
        self.cant = cantidad
        self.precio = precio
        
    def cantidad_actual(self):
        print("La cantidad actuial es: ", self.cant)
        
    def mostrar_precio(self):
        print("El precio es: ", self.precio)
        
    def vender(self, venta):
        if venta <= self.cant:
            self.cant -= venta
        else:
            print("Cantidad insuficiente")
 
    def comprar(self, compra):
        if compra > 0:
            self.cant += compra
 
Ejemplo1 = Articulo(901480430096, 15, 1500)
Ejemplo1.mostrar_precio()
Ejemplo1.vender(5)
Ejemplo1.comprar(20)
Ejemplo1.cantidad_actual()
Ejemplo1.vender(80)
Ejemplo1.cantidad_actual()
# Después de analizar el problema entendi que los atributos del trabajador eran el nombre, categoria, horas extras y tardanzas.
class Trabajador:
    def __init__(self, nombre, categoria, horas_extras, tardanzas):
      self.nombre = nombre 
      self.categoria = categoria
      self.horas_extras = horas_extras
      self.tardanzas = tardanzas
# Para facilitar el entendimiento del código, opte por poner in de "ingreso"_variable. Y como el problema pedía que los datos fueran ingresados por el usuario, puse el input.
print("================== DATOS DE ENTRADA ==================")
in_nombre = input("Nombre del trabajador........: ")
in_categoria = input("Ingrese una categoria........: ").upper()
while not (in_categoria == "A" or in_categoria == "B" or in_categoria == "C"): #Si la categoria no es A,B o C el bucle se repetira.
    print("Esa categoría no existe, ingrese A, B o C")
    in_categoria = input("Ingrese una categoria........: ").upper()
in_horas_extras = int(input("Ingrese horas extras.........: "))
while not (in_horas_extras >= 0): #Si las horas extras no es un valor positivo, el bucle se repetira. 
    print("Horas extras no puede ser un valor negativo.")
    in_horas_extras = int(input("Ingrese horas extras.........: "))
in_tardanzas = int(input("Ingrese Tardanza (minutos)...: "))
while not (in_tardanzas >= 0): #Si las tardanzas no es un valor positivo, el bucle se repetira. 
    print("Tardanzas no puede ser un valor negativo.")
    in_tardanzas = int(input("Ingrese Tardanza (minutos).........: "))
print("======================================================")

class Boleta_pago(Trabajador): #Boleta_pago heredara datos de trabajador para poder crear la boleta de pago.    
    def __init__(self, nombre, categoria, horas_extras, tardanzas):
      self.nombre = nombre 
      self.categoria = categoria
      self.horas_extras = horas_extras
      self.tardanzas = tardanzas
      self.sb = 0
      self.PH = 0
      self.PHX = 0
      self.tard = 0
      self.sn = 0
      
    #Definimos el método sueldo basico. Coloque un condicional, ya que según la categoria el sueldo basico varia. 
    def generarboleta (self): 
        if self.categoria == "A":
            self.sb = 3000
        elif self.categoria == "B":
            self.sb = 2500
        elif self.categoria == "C":
            self.sb = 2000
            
        self.PH = self.sb / 240
        self.PHX = self.PH * self.horas_extras
        # Como el descuento de tardanza, es en minutos se define como, PH / 60 multiplicado por los minutos de tardanza.
        self.tard = (self.PH / 60) * self.tardanzas
        # Definimos el sueldo neto
        self.sn = self.sb + self.PHX - self.tard
        
        print("================== DATOS DE SALIDA ===================")
        print("NOMBRE..................: ", self.nombre)
        print("CATEGORIA...............: ", self.categoria)
        print("SUELDO BASICO...........: ", self.sb)
        print("DESCUENTO TARDANZAS.....: ", round(self.tard,2)) #Round sirve para redondear y el ,2 para que sea a 2 decimales.
        print("PAGO HORAS EXTRAS.......: ", round(self.PHX,2))
        print("SUELDO NETO.............: ", round(self.sn,2))
        print("======================================================")
        
# Generamos la boleta.
Boleta1 = Boleta_pago(in_nombre, in_categoria, in_horas_extras, in_tardanzas)
Boleta1.generarboleta()
#Escribir un programa en pyhon para crear una clase cuenta bancaria con atributos de instancia: numero de cuenta, nombre del titular, balance

# atributos de la cuenta bancaria: Numero de cuenta, nombre del titular, balance inicial, balance actual, fecha de apertura....

# métodos o funcionalidades: retirar,depositar, generar balance, actualizar datos,.....

class Cuenta_bancaria :
    def __init__(self, numero_de_cuenta, nombre_del_titular, balance):
        self.nc = numero_de_cuenta
        self.nt = nombre_del_titular
        self.balance = balance
        
    def generar_balance(self):
        print(self.balance)
        
    def depositar(self, monto):
        if monto > 0:
            self.balance = self.balance + monto

Cliente1= Cuenta_bancaria(5510546448947777, "Kevin", 2000)

Cliente1.generar_balance()
Cliente1.depositar(500)
Cliente1.generar_balance()
Cliente1.depositar(400)
Cliente1.generar_balance()
Cliente1.depositar(600)
Cliente1.generar_balance()


'''
print("El numero de la cuenta es: ", Cliente1.nc)
print("El titular de la cuenta es: ", Cliente1.nt)
print("El balance de la cuenta es: ", Cliente1.balance)
'''
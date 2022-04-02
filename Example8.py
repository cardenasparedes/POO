# # Encapsulación:

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
        
#     def display_user(self):
#         print("User name is: ", self.name)
#         print("User age is: ", self.age)

# User1 = User("Jhon Doe", 35)

# # Llamando al método de la clase 
# User1.display_user()

# # Accediendo directamente a las variables
# User1.name
# User1.__age

# class Robot:
#     def __init__(self):
#         self.a = 123
#         self._b = 123
#         self.__c = 123
        
# yorobot = Robot()   

# print(yorobot.a)
# print(yorobot._b)
# print(yorobot._Robot__c)

class Car:
    maxspeed = 0
    name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.name = "SuperCar"
        
    def drive(self):
        print("Driving maxspeed ", self.__maxspeed)
        
    def setMaxSpeed (self, speed):
        self.__maxspeed = speed
        

bluecar = Car()
bluecar.drive()
bluecar.setMaxSpeed(400)
bluecar.drive()



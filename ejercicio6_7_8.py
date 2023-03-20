#from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    @property
    def imprimir_vacio(self):
        print("Nombre: ")
        print("Apellido: ")
        print("DNI: ")

    @property # Getters
    def nombre(self):
        return self.__nombre
    @nombre.setter #Seterrs
    def nombre(self, nombre):
        self.__nombre = valor
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad = 0
        else:
            self.__edad = edad
   
    @property
    def dni(self):
        return self.__dni
    
    #Validadr dni
    @property
    def validar_dni(self):
        letras = "qwertyuiopasdfghjklñzxcvbnm"
        if len(self.__dni)!=9:
           print("DNI incorrecto")
           self.__dni = ""
        else:
            try:
                num=int(self.dni)
            except:
                 print("DNI incorrecto")
                 self.__dni = ""

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
        self.validar_dni()

    @property
    def imprimir(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nDNI: {self.__dni}"

    
    def mayor_de_edad(self):
        return self.__edad>=18
        
#edad=int(input("Ingrese su edad: "))
#dni=input("Ingrese su DNI: ")
#nombre=input("Ingrese su nombre: ")       



#p1= Persona(nombre,edad,dni)
#p1.imprimir_vacio
#print(p1.mayor_de_edad())
#print(p1.imprimir)
#
print("Ejercicio7")
class Cuenta(): 
    def __init__(self, titular, cantidad=0):
        self.__titular = Persona (titular.nombre,titular.edad,titular.dni)
        self.__cantidad = cantidad
    
    #Datos vacios   
    
    def datos_vacio(self):
        print("Titular: ","\nCantidad: ")

    
    #Getters y setters
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad     
    #Saldo
    def saldo(self,cantidad):
        
          print(self.__titular.nombre,"Tiene en su cuenta la suma de: ",self.__cantidad)

    #Deposito
    def deposito(self, cantidad):        
       self.__cantidad = self.__cantidad + cantidad
       return f"Deposito la suma de: {self.cantidad}"
       
         
    #Retiro
    def retiro(self, cantidad):
        if cantidad > 0:
          self.__cantidad = self.__cantidad - cantidad
          return f"Retiro la suma de: {self.__cantidad}"
          
    

persona = Persona("Roberto", 20, 12345678)
cuenta=Cuenta(persona, 300)

cuenta.datos_vacio()
cuenta.saldo(300)
print(cuenta.retiro(100))
print(cuenta.deposito(100))

print("___________e")
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
        
        
    
    #Getters y Setters
    @property
    def bonificacion(self):
        self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    #Mostrar datos
     
    def mostrar(self):
        return f"Cuenta joven \nBonificacion: {self.__bonificacion}%"

   #Determinar si es mayor de adad
    
    def es_titular_valido(self):
        return self.titular.edad <= 25 and self.titular.edad >=18

    def retirar(self,cantidad):
        if not self.es_titular_valido():
            print("Titular no es valido, no puedes retirar dinero")
        elif cantidad >0:
            super().retirar(cantidad)
        
    
    
        
   

persona2=Persona("Daniel",20,1234355)
cj=CuentaJoven(persona2, 2000,20)
print(cj.es_titular_valido())
print(cj.mostrar())
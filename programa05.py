Nombre: Cristian Peralta Aviles
Matricula: 1722110292
Grupo: TI21
Fecha: 18/01/2024
En este codigo aprendimos a como realizar una suma, y unos mensajes en python
"""
class Alumno: #Define la clase
  matricula = None #Declara la variable matricula
  nombre = None #Declara la variable nombre
  def __init__(self, matricula, nombre): #Define el constructor
      self.matricula = matricula #Asigna el valor de matricula
      self.nombre = nombre #Asigna el valor de nombre
      print("Objeto Alumnos") #Imprime el mensaje
  def estudiar(self): #Define el metodo estudiar
      print(f"{self.nombre}estudia") #Imprime el mensaje
  def sumar(self, numero1, numero2): #Define el metodo sumar
      suma = numero1 + numero1 #Asigna el valor de la suma
      print(f"{numero1}+{numero2}={suma}") #Imprime el mensaje
dejah = Alumno(1111,"Dejah") #Crea un objeto de la clase Alumno
dejah.estudiar() #Llama al metodo estudiar
dejah.sumar(10,5) #Llama al metodo sumar

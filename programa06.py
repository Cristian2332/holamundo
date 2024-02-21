"""
ESTE ES UN EJEMPLO DE COMO CREAR UN DOCSTRING
    Nombre: Pancho TE 
    Fecha: 30/01/2023
    Descripcion: Programa que imprime el mensaje de bienvenida
""" #Es el Docstring


class Alumno:  #Define la clase
  nombre = None  #Define la variable

  def __init__(self, nombre):  #Define al constructor
    self.nombre = nombre  #Da valor a la variable
    print(f"Alumno {self.nombre} creado")  #Imprime el texto


dejah = Alumno("Dejah")  #Crea un objeto

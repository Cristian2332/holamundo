"""
Programa: eva01.py
Alumno:
Matricula:
Fecha:
"""
class Profesores:
    id = None
    nombre = None
    materias = [] # Array: Almacena varios valores


    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        print("Clase Profesor")


    def califica(self):
        print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre,self.materias[0])) #noc


    def pasaAsistencia(self):
        print(f"El profesor {self.nombre} pasa asistencia")


profesor1 = Profesores("111","Profesor 1")
profesor1.materias.append("Materia 1")
profesor1.materias.append("Materia 2")
profesor1.califica()
profesor1.pasaAsistencia()

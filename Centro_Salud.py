import Profesional
import Alerta
import Paciente
class Centro_Salud:

    #Atributos
    def __init__(self,i,n,d):
        self.ide=i
        self.nombre=n
        self.direccion=d
        self.alerta=["caca"]
    #Getters Setters
    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.ide
    def getDireccion(self):
        return self.direccion
    def getAlerta(self):
        return self.alerta

    def setNombre(self, nombre):
        self.nombre=nombre
    def setId(self, ide):
        self.ide= ide
    def setDireccion(self, direccion):
        self.direccion=direccion
    def setAlerta(self, alerta):
        self.alerta=alerta

    #Metodos
    def agregarPaciente(self):
        return True
    def eliminiarPaciente(self):
        return True
    def agregarProfesional(self):
        return True
    def eliminarProfesional(self):
        return True
    def mostrarPacientes(self):
        return True
    def mostrarProfesionales(self):
        return True
    def mostrarAlertas(self):
        return True
    def asignarAlertas(self, profesional, prioridad):
        return True
    def procesarAlertas(self, asignarAlertas):
        return True
    def colaPrioridades(self):
        return True

centro=Centro_Salud(1,2,3)
print(centro.getId())
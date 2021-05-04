class Profesional:
    
    #Atributos
    def __init__(self,r,n,a,f):
        self.rut=r
        self.nombre=n
        self.apellido=a
        self.fono=f

    #Getters Setters
    def getRut(self):
        return self.rut
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getFono(self):
        return self.fono
    
    def setRut(self,rut):
        self.rut=rut
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellido(self, apellido):
        self.apellido=apellido
    def setFono(self, fono):
        self.fono=fono
    
    #Metodos
    def editarFichaMedica(self):
        return True
    def verFicha(self, paciente):
        return True
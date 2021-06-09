class Profesional():
    
    #Atributos
    def __init__(self,Rut,Nombre,Apellido,Fono):
        super().__init__()
        self.rut=Rut
        self.nombre=Nombre
        self.apellido=Apellido
        self.fono=Fono

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
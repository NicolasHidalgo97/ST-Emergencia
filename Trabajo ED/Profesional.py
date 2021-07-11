class Profesional():
    
    #Atributos
    def __init__(self,Rut,Nombre,Apellido,Fono,Especialidad):
        super().__init__()
        self.rut=Rut
        self.nombre=Nombre
        self.apellido=Apellido
        self.fono=Fono
        self.especialidad=Especialidad

    def __str__(self):
        return str(self.nombre) +" "+ str(self.apellido)+" /rut: "+str(self.rut)+" "+str(self.especialidad)

    #Getters Setters
    def getRut(self):
        return self.rut
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getFono(self):
        return self.fono
    def getEspecialidad(self):
        return self.especialidad

    def setRut(self,rut):
        self.rut=rut
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellido(self, apellido):
        self.apellido=apellido
    def setFono(self, fono):
        self.fono=fono
    def setEspecialidad(self,especialidad):
        self.especialidad=especialidad
    
    
    #Metodos
    def editarFichaMedica(self):
        return True
    def verFicha(self, paciente):
        return True
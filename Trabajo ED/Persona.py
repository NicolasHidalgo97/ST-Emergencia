class Persona:
    def __init__(self,r,n,a,f):
        self.rut=r
        self.nombre=n
        self.apellido=a
        self.fono=f
    #Getters and Setters
    def getRut(self):
        return self.rut
    def setRut(self,rut):
        self.rut= rut
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre= nombre   
    def getApellido(self):
        return self.apellido
    def setApellido(self,apellido):
        self.apellido= apellido
    def getFono(self):
        return self.fono
    def setFono(self,fono):
        self.fono= fono
    #Metodos
    def editarDatos(rut):
        return True
#clases y objetos
#Crear clase 
class Alumno:
    nombre = "Daniel"
    cuenta = "2018"
    grado = 10
    #Metodos
    def mensaje(self):
        print("Este metodo extrae el nombre")

    def getCuenta(self):
        print(self.cuenta)

    def getGrado(self):
        return self.grado
    
    def verificar_Grado(self):
        if self.getGrado() == 10:
            print("Decimo grado")
        else:
            print("Otro grado")

#crear el objeto de la clase alumno
alumno_nuevo = Alumno()

#llamar metodos
alumno_nuevo.mensaje()
alumno_nuevo.getCuenta()
alumno_nuevo.verificar_Grado()


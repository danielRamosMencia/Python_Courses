#CLASE SUPER PADRE
class Animal:
    @property
    def terrestre(self):
        print("Animal terrestre")

#CLASE PADRE
class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

#CLASE PADRE
class Felino(Animal):
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino puede cazar")

#CLASE HIJA
class Gato(Felino, Mascota):

    def gato_cazador(self):
        self.cazar()

    #Override: Sobre Escritura de metodos en las clases heredadas
    def mostrar_nombre(self):
        #Llamar un metodo sobrescrito
        Mascota.mostrar_nombre(self)
        print("El nombre del gato es: {}".format(self.nombre))

g = Gato("Michi")
g.mostrar_nombre()
#CLASE SUPER PADRE
class Animal:
    @property
    def terrestre(self):
        print("Animal terrestre")

#CLASE PADRE
class Felino(Animal):
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino puede cazar")

#CLASE HIJA
class Gato(Felino):
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino):
    pass

g1 = Gato()
j1 = Jaguar()

print(g1.gato_cazador())
print(j1.terrestre)
print(g1.cazar())
print(j1.cazar())

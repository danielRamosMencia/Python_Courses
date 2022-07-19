class Animal:
    volador = True

class Cocodrilo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
    
    #EL METODO PERTENECE A LA CLASE Y NO A LA INSTANCIA
    @classmethod
    def new(cls, nombre):
        return Cocodrilo(nombre)

c = Cocodrilo.new("coco")
print(c.nombre)
print(c.volador)


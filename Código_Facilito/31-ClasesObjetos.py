""" La programacion orientado a objetos es un paradigma de programacion
Cada objeto tiene ciertas caracteristicas y puede generar ciertas accio-
nes.
"""
#Usar camelCase para los nombre de las clases
class Lapiz:
    
    #CONSTRUCTOR DE LA CLASE
    def __init__(self, color, have_eraser, use_graphit):
        #ATRIBUTOS DE LA CLASE
        self.color = color
        self.have_eraser = have_eraser
        self.use_graphit = use_graphit

    #METODOS DE LA CLASE
    def dibujar(self):
        print("El lapiz esta dibujando")

    def borrar(self):
        #ANIDAR METODOS DENTRO DE LA MISMA CLASE
        if self.can_erase() == True:
            print("Puede borrar")
        else:
            print("No puede borrar")

    def can_erase(self):
        return self.have_eraser
    
n_Lapiz = Lapiz("Rojo", False, True)
n_Lapiz.dibujar()
n_Lapiz.borrar()


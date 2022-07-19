class Circulo:
    """
    #VARIABLE DE CLASE, LE PERTENECEN A LA CLASE Y NO A LOS OBJETOS
    #_nombreVariable convencion para no modificar las variables de clase
    _pi = 3.1416
    """
    @staticmethod
    def pi():
        return 3.1416

    def __init__(self, radio):
        self.radio = radio

    #METODOS DE INSTANCIA: Tienen el parametro self y se encuentra dentro de la clase
    def area(self): 
        area_c = self.radio * self.radio * Circulo.pi()
        return area_c

    
print(Circulo.pi())
c1 = Circulo(7)
print(c1.area())


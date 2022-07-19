#Laboratorio Inteligencia Artificial - Miercoles 15 de Junio
#Alumno: Daniel Eduardo Ramos Mencía
#Cuenta: 20181006956
class Vector:
    #constructor: metodo init
    def __init__(self, elemento):
        """Inicializa el vector con la lista elementos.
        Lanza una excepción de tipo TypeError en caso de que elementos no sea una
        lista de números flotantes.
        """
        if not isinstance(elemento, list):
            raise TypeError("El elemento no es una lista")
        
        for i in range(len(elemento)):
            if not isinstance(elemento[i], float):
                raise TypeError("El elemento de la lista no es un flotante")

        self._elemento = elemento

    #Sumar dos vectores que son objetos de la clase vector
    def sumar(self, vec):
        """Retorna la suma del vector actual con el parámetro <vector>
        Lanza una excepción de tipo TypeError en caso de que <vector> no sea de 
        tipo Vector.
        Lanza una excepción de tipo ValueError en caso de que <vector> no tenga
        las mismas dimensiones del vector actual.
        """ 
        sub_lista = vec.elementos()
        lista_sumas = []
        vrb_suma = 0
        if not isinstance(vec, Vector):
            raise TypeError("El vector a sumar no es de la clase Vector")

        if len(self._elemento) != vec.size():
            raise ValueError("El tamanio de los vectores es distinto")
            
        for i in range(len(self._elemento)):
            vrb_suma = self._elemento[i] + sub_lista[i]
            lista_sumas.append(vrb_suma)
        
        resolucion = Vector(lista_sumas)
        return resolucion
        

    #Producto punto
    def prod_punto(self, vec):
        """Retorna el producto punto del vector actual con el parámetro <vector>
        Lanza una excepción de tipo TypeError en caso de que <vector> no sea de 
        tipo Vector.
        Lanza una excepción de tipo ValueError en caso de que <vector> no tenga
        las mismas dimensiones del vector actual.
        """
        X = vec.elementos()
        Y = Vector(X)
        factor = 0
        contador = 0
        
        if not isinstance(vec, Vector):
            raise TypeError("El vector del producto no es de la clase Vector")
        
        if len(self._elemento) != vec.size():
            raise ValueError("El tamanio de los vectores es distinto")

        for i in range(len(self._elemento)):
            factor = (self._elemento[i] * Y._elemento[i]) 
            contador = contador + factor

        return contador

    #Extraer el tamanio
    def size(self):
        """Retorna el número de elementos en el vector"""
        tamanio = len(self._elemento)
        return tamanio

    #Extraer los elementos y colocarlos dentro de una lista
    def elementos(self):
        """Retorna una lista con los elementos del vector"""
        sub_lista = []
        for i in range(len(self._elemento)):
            sub_lista.append(self._elemento[i])
        
        return sub_lista
    
    def __str__(self):
        """Método especial de python que retorna el vector como str.
        Se proporciona la implementación (no hay que cambiar nada).
        """
        return str(self.elementos())
    

A = [4.0, 5.0, 6.0]
B = [1.0, 2.0, 3.0]

v1 = Vector(A)
v2 = Vector(B)

v3 = v1.sumar(v2)
print(v3)

v4 = v2.sumar(v1)
print(v4)

escalar = v1.prod_punto(v2)
print(int(escalar))








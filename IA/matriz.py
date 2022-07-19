### Ejercicio:
# Implemente los métodos de la clase Matriz para que funciones de acuerdo a
# lo que indican sus cadena de documentación.
#
# Antes de subir su ejercicio al campus virtual compruebe su correctiud
# en el siguiente enlace:
#   https://rp-autograder.herokuapp.com/
# 
# Para la entrega suba este archivo con el mismo nombre que tiene: "matriz.py"
# No lo comprima ni lo coloque dentro de un directorio.
#
# PD: El texto después del caracter '#' en Python es un comentario.
# La palabra 'pass' puede borrarla cuando haya puesto código al método.

class Matriz:

  # Matriz([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
  def __init__(self, elementos):
    """Inicializa una matriz bidimensional recibe una lista de listas con los
    elementos.
    Lanza una excepción de tipo TypeError en los siguientes casos:
      - Si elementos no es una lista.
      - Si los elementos dentro de los elementos no son listas.
      - Si los elementos dentro de las listas no son enteros o flotantes.
    Lanza una excepción de tipo ValueError si alguna de las listas internas
    tiene tamaño diferente al resto.
    """
    pass
  
  def sumar(self, matriz):
    """Retorna la suma de la matriz actual con el parámetro <matriz>
    Lanza una excepción de tipo TypeError en caso de que <matriz> no sea de 
    tipo Matriz.
    Lanza una excepción de tipo ValueError en caso de que <matriz> no tenga
    las mismas dimensiones que la matriz actual.
    """
    pass

  def dimensiones(self):
    """Retorna una tupla con las dimensiones de la matriz (n,m).
    Donde <n> es el número de filas y <m> el número de columnas.
    """
    pass

  def elementos(self):
    """Retorna una lista de listas con los elementos de la matriz"""
    pass

  def __str__(self):
    """Método especial de python debe retornar la matriz como str.
    Ej.: [[1,2],[3,4]]
    """
    pass
  

## Ejemplo de uso ##

# m1 = Matriz([[1,2,3],[4,5,6]])
# print(m1)
# m2 = Matriz([[1,1,1],[1,1,1]])
# print(m2)

# m3 = m1.sumar(m2)
# print(m3)  # Debería de imprimir [[2, 3, 4],[5, 6, 7]]
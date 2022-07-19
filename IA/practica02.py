class Matriz:
    def __init__(self, elementos):
        if not isinstance(elementos, list):
            raise TypeError("EL ELEMENTO NO ES UNA LISTA")
        for i in range(len(elementos)):
            if not isinstance(elementos[i], list):
                raise TypeError("EL ELEMENTO DEL ELEMENTO NO ES UNA LISTA")
            for j in range(len(elementos[i])):
                if not isinstance(elementos[i][j], (int,float)):
                    raise TypeError("EL ELEMENTO DENTRO DEL ELEMENTO NO ES UN ENTERO O FLOTANTE")
        self.elementos = elementos

M = [[1,2,3],[4,5,6]]

try:
    mi_matriz = Matriz(M)
    print(mi_matriz.elementos)
except TypeError as e0:
    print(e0)
    print("HA OCURRIDO UN ERROR")
except ValueError as e1:
    print(e1)
    print("HA OCURRIDO UN ERROR")
finally:
    print()
    print("***PROGRAMA TEMINADO***")
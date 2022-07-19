M = [[1,2,3],[4,5,6],[7,8,9]]
N = [[1,1,1],[2,2,2],[3,3,3]]

#for q in range(len(N)):
#   for r in range(len(N[q])):
#        print(N[q][r])

def dimensiones(matriz):
    contador_columnas = 0
    contador_filas = 0
    for i in range(len(matriz[0])):
        contador_columnas = contador_columnas + 1

    for j in range(len(matriz)):
        contador_filas = contador_filas + 1

    tupla_dimensiones = (contador_filas, contador_columnas)

    return tupla_dimensiones

#T = dimensiones(M)
#print(T)

def sumar(matriz, factor):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            contador = contador + matriz[i][j] + factor[i][j]

    return contador

#S = sumar(M, N)
#print(S)

def elementos(matriz):
    sub_lista = []

    for i in range(len(matriz)):
        sub_lista.append(matriz[i]) 

    return sub_lista

L = elementos(M)
print(L)




    
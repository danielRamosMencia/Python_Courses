"""
# FORMA EXTENSA
lista = []
for valor in range(0,101):
    lista.append(valor)

print(lista)
"""

lista = [ v for v in range(0, 51) if v % 2 == 0]
#v: valor a agregar a la lista
#ciclo: for
#se puede agregar condicionales dentro de los comprehension
print(lista)

tupla = tuple(( x for x in range(0, 51) if x % 2 != 0))
print(tupla)

diccionario = { indice:valor for indice, valor in enumerate(lista)}
print(diccionario)
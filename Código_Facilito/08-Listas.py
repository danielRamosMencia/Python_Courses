#Tipo de dato que es una secuencia que puede almacenar distintos tipos de datos
l = ["Strings", 1, 2.5, True]
print(l)
#agregar un elemento al final de la lista
l.append("object")
print(l)
#agregar un elemento en una posicion
l.insert(0, "index")
print(l)
#borrar un elemento
l.remove(1)
print(l)
#obtener un ultimo valor
last = l.pop()
print(last)

#ordenar de forma ascendete los numeros de una lista
l2 = [1,5,76,23,90,23,13,5]
print(l2)
l2.sort()
print(l2)
#ordenar de forma descente
l2.sort(reverse=True)
print(l2)
#unir dos listas
l3 = [1,2,3,4,5]
l2.extend(l3)
print(l2)
l2.append(l)
print(l2)
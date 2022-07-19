#String = Lista de caracteres
x = "Curso de python"
#Generar un string en base a otro
y = x[0:8]
print(x)
print(x[0] + x[1])
print(x[0] + "%s" %(x[1]))
print(x[0] + x[-1])
#imprimir una parte de la lista, un string generado en base a otro
print(x[0:8])
print(x)
print(y)
print(y[0:10:2])
#leer en reversa
print(x[::-1])
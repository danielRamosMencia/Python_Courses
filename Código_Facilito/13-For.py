lista = [1,2,3,4,5,6,7,8,9,10]
tupla = (11,12,13,14,15,16,17,18,19,20)
diccionario = {"a":10, "b":20, "c":30}

#Generar un objeto iterable
for ind, i in enumerate(tupla):    
    print(i, "indice: ", ind)

for i in range(len(lista)):
    print(i)

for llave, valor in diccionario.items():
    print("LLave: ", llave, "Valor: ", valor)
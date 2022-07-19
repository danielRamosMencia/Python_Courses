introduccion = """---BUSCADOR DE LETRAS---
Ingrese una frase:"""
print(introduccion)
frase = input()

print("Ingrese un caracter a buscar:")
caracter = input()
contador = 0

for i in frase:
    if i == caracter:
        contador += 1
        break

if contador != 0:
    print("Caracter encontrado")
else:
    print("No se encontro el caracter")



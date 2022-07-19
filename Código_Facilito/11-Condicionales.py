fruta = 'manzana'

if fruta == "m":
    print("es una manzana")
else:
    print("no es una manzana")

msj = "Daniel" if fruta == 'manzana' else False
print(msj)

if fruta == "m":
    print("1")
elif fruta == "a":
    print("2")
elif fruta == "manzana":
    print(True)
else:
    print("3")
""" 
CUALQUIER OBJETO VACIO TIENE UN VALOR FALSO"""
if 0:
    print("Verdad")
else:
    print("Falso")

v1 = 2
v2 = False

if v1 == 2 and v2 == False:
    print(True)
elif v1 == 2 or v2:
    print("VERDAD")
else:
    print("omitir")
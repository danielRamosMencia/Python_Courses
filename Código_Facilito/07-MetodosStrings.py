""" METODOS DE FORMATO"""
c = "CURSO"
v = "python"

r = "{} de {}".format(c, v)
print(r)

r2 = "{a} {b}".format(a = "daniel", b = "ramos")
print(r2)
#colocar todo en minusculas
#lower nos da como salida otro string no modifica el original
r3 = r.lower()
r4 = r.upper()
print(r3)
print(r4)
#Colocar un string como titulo
r5 = r.title()
print(r5)

"""METODOS DE BUSQUEDA """
bus = r.find('C')
print(bus)
print(r[bus])
cont = r.count('C')
print(cont)

""" METODOS DE SUSTITUCION"""
nuevo = r.replace('C', 'd')
print(nuevo)
nuevo2 = r.split(" ")
print(nuevo2)

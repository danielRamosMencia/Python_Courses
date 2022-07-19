l = [1,2,3]
t = [True, False]
d = {"A":10, "B":20, "C":True, "D":l, "E":t}
print(d["D"])
print(d["E"])

#AGREGAR ELEMENTO A DICCIONARIO
#SI SE ENCUENTRA LA CLAVE SE REEMPLAZA, SINO CREA
d["F"] = "Daniel"
print(d)
d["A"] = False
print(d)

#OBTENER UN VALOR 
vrb = d["A"]
print(vrb)

#METODO para saber si hay una clave dentro del diccionario
vrb2 = d.get("Z", 0)
print(vrb2)

#ELIMINAR
del d["B"]
print(d)

#OBTENER UN OBJETO ITERABLE CON TODAS LAS LLAVES
k = d.keys()
v = d.values()
k = list(k)
v = list(v)
print(k)
print(v)

#EXTENDER DICCIONARIO
d2 = {"S":1, "Q":2}
d.update(d2)
print(d)
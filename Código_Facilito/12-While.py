c = 0
l = []
while c <= 10:
    print(c)
    c += 1
    if c % 2 == 0:
        l.append(c)
        continue
    elif c > 8:
        print(l)
        break
else:
    print("FIN DEL CICLO")
    print(l)

terminar = False
x = 0

while terminar == False:
    x += 1
    print("Hola {}".format(x))
    if x == 5:
        terminar = True
else:
    print("FIN DEL CICLO")
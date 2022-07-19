import random
import datetime as dt
import sys
import time

#generar un numero aleatorio entre el 0 y 10 incluidos
valor = random.randint(0, 10)
print(valor)

#obtener un elemento aleatorio en una lista 
l = [1,2,3,4,5,6,7]
valor = random.choice(l)
print(valor)

#desordenar una lista
print(l)
random.shuffle(l)
print(l)

#fechas
print(dt.datetime.now())
#generar un conteo de progreso
for i in range(101):
    #generar delay
    time.sleep(0.1)
    sys.stdout.write("\r%d %%" % i)
    sys.stdout.flush()




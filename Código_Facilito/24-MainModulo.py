#Los modulos se colocan en el mismo nivel para mayor facilidad
#import Calculadora as c
#r = c.suma(10, 25)
#print(r)
from Calculadora import __name__ as __name__calculadora__
from Calculadora import resta
from Calculadora import producto
from Calculadora import division as div

r1 = resta(10,2)
print(r1)

r2 = producto(10, 3.5)
print(r2)

r3 = div(100, 20)
print(r3)

print(__name__)
print(__name__calculadora__)

if __name__ == "__main__":
    print("Es el scipt principal")

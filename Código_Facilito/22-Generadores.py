#Los generadores nos ayudan a crear objetos sin necesidad de almacenarlos en memoria RAM
def generator(*args):
    for i in args:
        yield i * 10, True #yield toma el valor para regresarlo en la iteracion posterior

for valor, valor1 in generator(1,2,3,4,5):
    print(valor, valor1)
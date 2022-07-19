def my_decorator(func):# funcion que ejecuta todo
    def new_function(*args, **kwargs):#funcion  que se le aplican nuevas funcionalidades
        print("PASO 1")
        resultado = func(*args, **kwargs)
        print("FUNCION EJECUTADA")
        return resultado
    return new_function#retorno de la nueva funcion con otras funcionalidades

@my_decorator
def gretting():
    print("Hola mundo")

@my_decorator
def suma(n1, n2):
    return n1 + n2

gretting()
s = suma(10, 20)
print(s)


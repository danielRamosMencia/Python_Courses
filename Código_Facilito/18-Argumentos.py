
def suma(*arguments):
    print(type(arguments))
    r = 0
    for v in arguments:
        r = r + v
    return r

result = suma(1,2,3,4,5,6,7)
print(result)

def my_function(**args):
    print(args)
    return None

#result = my_function(valor = "Daniel", x = 1, y = 0.75, z = True)
print(result)

# * n parametros con tuplas
# ** n parametros con diccionarios

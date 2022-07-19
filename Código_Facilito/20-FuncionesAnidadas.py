#Closure, funciones que crean otras funciones
def crear_funcion(x1, x2):
    def validacion():
        print("VALIDACION   ")
        return x1 > 0 and x2 > 0
    return validacion
    
def apply_function(func):
    result = func()
    print(result)

new_function = crear_funcion(10, 2)
apply_function(new_function)


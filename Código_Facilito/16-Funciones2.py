def suma(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4

resultado = suma(1,2,3,5)
print(resultado)

def division(n1, n2):
    return n1 / n2

resultado = division(100, 10)
print(resultado)

def percent(v, m, factor = 100):
    p = m / factor
    v = v * p
    return v

porcentaje = percent(50, 50)
print(porcentaje)

#Retornar multiples valores
def multi_value():
    return "String", 1, True, 25.6

string, entero, bol, flotante = multi_value()
print(string)
print(entero)
print(bol)
print(flotante)

#asignar una funcion a una variable
alias = percent
my_number = alias(100, 50)
print(my_number)


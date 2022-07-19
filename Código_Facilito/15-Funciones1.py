def f_factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

mi_factirial = f_factorial(3)
print(mi_factirial)

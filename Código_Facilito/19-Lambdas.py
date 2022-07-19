my_function = lambda v1, v2 : v1 + v2
my_format = lambda my_sentence : "!{}?".format(my_sentence)
whithout_return = lambda : print("SIN RETORNO")
result = my_function(5, 6)
print(result)
phrase = my_format("Mi frase")
print(phrase)
variable = whithout_return
print(variable)
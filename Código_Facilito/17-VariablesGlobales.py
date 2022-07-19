def palindromo(sentence):
    new_value = sentence.replace(" ", "")
    return new_value == new_value[::-1]

my_sentence = "anita lava la tina"
print(my_sentence)
r = palindromo(my_sentence)
print(r)

def global_value():
    global global_lvariable
    global_variable = "Cambiar valor"

global_variable = "Variable global"
print(global_variable)
global_value()
print(global_variable)
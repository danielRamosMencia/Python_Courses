data = [1,2,3,4,5]

def escala(mi_lista, factor = 5):
    for i in mi_lista:
        i *= factor
        print(i)

escala(data)
try:
    l = [1,2]
    print(l[3])
    #print(2/0)
except ZeroDivisionError as ex:
    print(ex)
    print("No se puede dividir entre 0")
except IndexError as ex:
    print(ex)
    print("No existe ese elemento en la lista")
except Exception as E:
    print(E)
    print("OCURRIO UN ERROR")
finally:
    print("Se terminó el script")
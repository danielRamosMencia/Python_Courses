try:
    lista = [1,2]
    print(lista[9])
except ZeroDivisionError as e:
    print(e)
    print("No es posible dividir entre 0")
except IndexError as e:
    print(e)
    print("No existe un elemento en ese indice ")
#Manejo de error generico
except Exception as e:
    print(e)
    print("Ha ocurrido un error")
#opcional
#Este bloque va a ejecutarse siempre
finally:
    print("***FIN DEL PROGRAMA***")

def generator(*args):
    """Recibe una n cantidad de numero y regresa el numero ademas de
    regresar True o False si el numero es mayor 5
    """ 
    for valor in args:
        yield valor, True if valor > 5 else False

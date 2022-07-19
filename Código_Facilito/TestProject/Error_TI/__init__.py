from .validations import validation_tiny_int, my_ftiny_int
from .errorClass import TinyIntError

def my_tiny_int(t):
    try:
        if validation_tiny_int(t) and tiny_int(t):
            return True
        else:
            raise TinyIntError()   
    except TinyIntError as error:
        print(error)   
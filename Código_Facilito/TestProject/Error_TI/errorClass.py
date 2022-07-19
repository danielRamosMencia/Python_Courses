class TinyIntError(Exception):   
    def __init__(self):
        self.message = "El numero no cuenta con las caracteristicas de un TINYINT"

    def __str__(self):
        return self.message
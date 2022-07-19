class Usuario:
    def __new__(cls):
        print("Este metodo es el primero que se ejecuta")
        return super().__new__(cls)

    def __init__(self):
        print("Este metodo es el segundo que se ejecuta")

    def __str__(self):
        return "Esto se imprime cuando intento mostrar el objeto"

    def __getattr__(self, nombre):
        print("No se encontro el atributo****")
        self.otro_metodo()

    def otro_metodo(self):
        print("otro metodo")
        

user = Usuario()
print(user)

print(user.apellido)



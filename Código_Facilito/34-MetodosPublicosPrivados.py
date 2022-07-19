class Usuario:
    def __init__(self, nombre, password, email):
        self.nombre = nombre
        #ATRIBUROS PRIVADOS: ANTEPONER DS GUIONES BAJOS __
        self.__password = self.__generate_password(password)
        self.email = email

    #METODO PRIVADO: ANTEPONER DS GUIONES BAJOS __
    def __generate_password(self, password):
        return password.upper()

    #PROPERTIES
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, valor):
        self.__password = self.__generate_password(valor)


n_user = Usuario("Daniel", "enay123", "derm@gmail.com")
print(n_user.password)
n_user.password = "NEWPASSWORD"
print(n_user.password)

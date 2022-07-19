class Personas:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

nueva_persona = Personas("Daniel", 21, True)

print(nueva_persona.nombre)
print(nueva_persona.edad)
print(nueva_persona.sexo)



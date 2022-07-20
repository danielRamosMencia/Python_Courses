import PySimpleGUIQt as sg

form = sg.FlexForm("My Firts GUI")

layout = [  [sg.Text("Enter your name", size = (20, 2)),  sg.InputText()],
            [sg.Text("Enter your age", size = (20, 2)),  sg.InputText()],
            [sg.Text("Enter your ID", size = (20, 2)), sg.InputText()],
            [sg.Text("Enter your phone", size = (20, 2)), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

button, values = form.Layout(layout).Read()
#Mostrará en consola los valores retornando un diccionario con las claves 
#que son números y los valores digitados en el input
name = values[0]
age = values[1]
ID = values[2]
phone = values[3]
print(f"Name: {name}, Age: {age}, ID: {ID}, Phone {phone}")
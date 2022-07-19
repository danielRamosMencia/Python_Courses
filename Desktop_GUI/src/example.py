import PySimpleGUIQt as s
#PARA CREAR GUI WEB instalar PysSimpleGUIWeb

#Para agregar Widgets modificamos el parametro --layout--
#Con ello podemos agregar ventanas de diálogo, botones, etc.
#El parametro recibe listas para ordenar los widgets
#Cada lista es una fila de elementos o widgets
my_layout = [[s.Text("Mi primer app de escritorio con python"), 
            s.Button("Hello World")],
            [s.Button("OK"), 
            s.Button("Cancel"),
            s.Button("Maybe")]]

window = s.Window(title="hello world", size=(640, 480), layout=my_layout)


window.read()
from tkinter import *
import tkinter
from os import system

#############################
#   Ventanas principales    #
#############################

ventana = Tk()
#ventana.geometry("410x650")
ventana.attributes('-fullscreen', True)


titulo = tkinter.Label(
ventana,
text = "Smart Locker",
bg = "gray",
fg = "white",
font=("",10)
)

#Mostrando título en la ventana, centrado y superior
#titulo.grid(row = 0, column = 1)
titulo.pack(fill = tkinter.X)

##################
#   funciones    #
##################

def registrar():
    exec(open("Ventana_nuevo_usuario.py").read())

def ingresar():
    system(f"lxterminal -e python3 Validación_usuario.py")


#############
#   Botones #
#############

boton_registrar = Button(
ventana,
text = 'Nuevo registro',
command = registrar,
width = 30,
height = 4,
font=("",10)
)

boton_ingresar = Button(
ventana,
text = 'Ingresar con usuario existente',
command = ingresar,
width = 30,
height = 4,
font=("",10)
)



salir = Button(
ventana,
text = 'Salir',
command= ventana.destroy,
width = 30,
height = 4,
font=("",10)
)


#############################
#   Posición de los Botones #
#############################

#boton_mapa.grid(fila = 1, columna = 0)
#boton_mapa.grid(row = 1, column = 0)
boton_registrar.pack()
boton_ingresar.pack()


salir.pack()



# Mostrando ventana
ventana.mainloop()

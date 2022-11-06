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
font=("",30)
)

#Mostrando título en la ventana, centrado y superior
#titulo.grid(row = 0, column = 1)
titulo.pack(fill = tkinter.X)

##################
#   funciones    #
##################

def usuario():
    exec(open("Ventana_usuario.py").read())
    #reconocimiento = system(f"gnome-terminal -- python3 Reconocimiento/ReconocimientoFacial.py")

def admin():
    exec(open("Admin.py").read())

#############
#   Botones #
#############

boton_usuario = Button(
ventana,
text = 'Usuario',
command = usuario,
width = 50,
height = 4,
font=("",20)
)

boton_admin = Button(
ventana,
text = 'Modo administrador',
command = admin,
width = 50,
height = 4,
font=("",20)
)

salir = Button(
ventana,
text = 'Salir',
command= ventana.destroy,
width = 50,
height = 4,
font=("",20)
)


#############################
#   Posición de los Botones #
#############################

#boton_mapa.grid(fila = 1, columna = 0)
#boton_mapa.grid(row = 1, column = 0)
boton_usuario.pack()
boton_admin.pack()


salir.pack()



# Mostrando ventana
ventana.mainloop()

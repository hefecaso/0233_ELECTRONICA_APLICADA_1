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
font=("",20)
)

#Mostrando título en la ventana, centrado y superior
#titulo.grid(row = 0, column = 1)
titulo.pack(fill = tkinter.X)

##################
#   funciones    #
##################

def reconocimiento():
    exec(open("ReconocimientoFacial.py").read())


#############
#   Botones #
#############

boton_reconocimiento = Button(
ventana,
text = 'Reconocimiento facial',
command = reconocimiento,
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
boton_reconocimiento.pack()


salir.pack()



# Mostrando ventana
ventana.mainloop()
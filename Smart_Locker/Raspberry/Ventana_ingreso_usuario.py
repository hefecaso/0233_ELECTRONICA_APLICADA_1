from tkinter import *
import tkinter
from os import system
from tkinter import messagebox

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

# def guardar_rostro():
#     #exec(open("capturandoRostros.py").read())
#     system(f"lxterminal -e python3 capturandoRostros.py") #Ubuntu
#     #system(f"lxterminal -e python3 capturandoRostros.py")  #Raspberry
#     exec(open("entrenandoRF.py").read())

def reconocimiento():
    exec(open("ReconocimientoFacial.py").read())

    #system(f"lxterminal -e python3 Led-buscar_locker.py")

#def ingresar_nickname():
    #messagebox.showinfo("Hola!", "Hola mundo")

# Campo para pedir datos

#############


# username = tkinter.Entry(ventana, width = 20)
# username.pack()
#Button(username, text = "Button", )



#############
#   Botones #
#############

# boton_guardar_rostro = Button(
# ventana,
# text = 'Capturar rostro',
# command = guardar_rostro,
# width = 30,
# height = 4,
# font=("",10)
# )

boton_reconocimiento = Button(
ventana,
text = 'Abrir locker',
command = reconocimiento,
width = 30,
height = 4,
font=("",10)
)


# boton_ingresar_nickname = Button(
# ventana,
# text = 'Boton de prueba',
# command = ingresar_nickname,
# width = 30,
# height = 4,
# font=("",10)
# )


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
#boton_guardar_rostro.pack()
boton_reconocimiento.pack()
#boton_ingresar_nickname.pack()


salir.pack()



# Mostrando ventana
ventana.mainloop()

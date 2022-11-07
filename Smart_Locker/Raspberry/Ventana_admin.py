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

def datos_usuarios():
    system(f"lxterminal -e python3 Ver_usuarios_mod_admin.py")

def refresh():
    system(f"lxterminal -e python3 entrenandoRF.py")
    #exec(open("entrenandoRF.py").read())

def agregar_quitar_admin():
    system(f"lxterminal -e vim .Administrator/Administrator.csv")

def limpiar():
    system(f"lxterminal -e python3 Eliminar_archivos_antiguos.py")
    system(f"lxterminal -e python3 Eliminar_carpetas_antiguas.py")

#############
#   Botones #
#############

boton_datos_usuarios = Button(
ventana,
text = 'Ver archivos de los usuarios',
command = datos_usuarios,
width = 15,
height = 4,
font=("",10)
)

boton_refresh = Button(
ventana,
text = 'Refrescar y entrenar IA',
command = refresh,
width = 15,
height = 4,
font=("",10)
)

boton_agregar_quitar_admin = Button(
ventana,
text = 'Agregar/quitar administrador',
command = agregar_quitar_admin,
width = 15,
height = 4,
font=("",10)
)

boton_limpiar = Button(
ventana,
text = 'Eliminar archivos con más de un mes',
command = limpiar,
width = 15,
height = 4,
font=("",10)
)

salir = Button(
ventana,
text = 'Salir',
command= ventana.destroy,
width = 15,
height = 4,
font=("",10)
)


#############################
#   Posición de los Botones #
#############################

#boton_mapa.grid(fila = 1, columna = 0)
#boton_mapa.grid(row = 1, column = 0)
boton_datos_usuarios.pack()
boton_refresh.pack()
boton_agregar_quitar_admin.pack()
boton_limpiar.pack()

salir.pack()



# Mostrando ventana
ventana.mainloop()

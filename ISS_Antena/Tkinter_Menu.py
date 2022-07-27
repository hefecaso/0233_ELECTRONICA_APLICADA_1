from tkinter import *
import tkinter
from os import system

#############################
#   Ventanas principales    #
#############################

ventana = Tk()
ventana.geometry("500x795")

titulo = tkinter.Label(
ventana,
text = "ISS antenna program",
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

def elevacion():
    elevacion = system(f"lxterminal -e python3 servo.py")

def azimut():
    azimut = system(f"lxterminal -e python3 stepper.py")

def azimut_elevacion():
    system(f"lxterminal -e python3 servo.py")
    system(f"lxterminal -e python3 stepper.py")

    system("lxterminal -e python3 isschris2.py")

    system("lxterminal -e python3 brujula.py")

def target_iss():
    # Abriendo mapa
    system("lxterminal -e python3 isschris2.py")

    # Movimientos
    system(f"lxterminal -e python3 servotarget.py")
    system(f"lxterminal -e python3 steppertarget.py")

    system("lxterminal -e python3 brujula.py")

def mapa():
    # Para Raspbian
    mapa = system("lxterminal -e python3 isschris2.py")
    # Para Ubuntu
    #mapa = system("gnome-terminal -- python3 isschris2.py")

def brujula():
    brujula = system("lxterminal -e python3 brujula.py")

def origen():
    #print("\nRegresando a elevación 0°: \n")

    #print("Moviendo servo a 0°")

    system(f"lxterminal -e python3 servo_origin.py")

    #print("\nRegresando a azimut 0°: \n")

    exec(open("stepper_origin.py").read())
    GPIO.cleanup()
    time.sleep(5)
    #print("\n")

#############
#   Botones #
#############

boton_elevacion = Button(
ventana,
text = 'Control de elevación',
command = elevacion,
width = 40,
height = 4,
font=("",11)
)

boton_azimut = Button(
ventana,
text = 'Control del azimut',
command = azimut,
width = 40,
height = 4,
font=("",11)
)

boton_azimut_elevacion = Button(
ventana,
text = 'Control manual de la elevación y azimut',
command = azimut_elevacion,
width = 40,
height = 4,
font=("",11)
)

boton_target_iss = Button(
ventana,
text = 'Seguir trayectoria de la ISS (Auto)',
command = target_iss,
width = 40,
height = 4,
font=("",11)
)

boton_mapa = Button(
ventana,
text = 'ISS Tracker',
command = mapa,
width = 40,
height = 4,
font=("",11)
)

boton_origen = Button(
ventana,
text = 'Posicionar antena al Norte',
command = origen,
width = 40,
height = 4,
font=("",11)
)

boton_brujula = Button(
ventana,
text = 'Ver brujula',
command= brujula,
width = 40,
height = 4,
font=("",11)
)

salir = Button(
ventana,
text = 'Salir',
command= ventana.destroy,
width = 40,
height = 4,
font=("",11)
)


#############################
#   Posición de los Botones #
#############################

#boton_mapa.grid(fila = 1, columna = 0)
#boton_mapa.grid(row = 1, column = 0)
boton_elevacion.pack()
boton_azimut.pack()
boton_azimut_elevacion.pack()
boton_target_iss.pack()
boton_mapa.pack()
boton_origen.pack()
boton_brujula.pack()
salir.pack()



# Mostrando ventana
ventana.mainloop()

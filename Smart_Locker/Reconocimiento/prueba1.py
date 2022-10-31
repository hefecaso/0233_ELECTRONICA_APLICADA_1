import getpass
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

Nombre = input("Escriba su nombre ")
Contraseña = getpass.getpass("Ingrese su contraseña ")
Locker = int(input("Digite el numero de locker que desea "))
Dpi = int(input("Digite su numero de identificacion personal "))

#savetxt("Nombre.csv", array([Nombre,Contraseña,Locker,Dpi]).T , delimiter=",", header='Nombre,Contraseña,Locker,Dpi')

df = pd.DataFrame([[Nombre,Locker,Dpi]], columns = ['Nombre', 'Locker', 'Dpi'])
df.to_csv(Nombre)

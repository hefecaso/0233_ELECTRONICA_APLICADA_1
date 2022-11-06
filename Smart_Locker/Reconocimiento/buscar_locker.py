import pandas as pd

Username = input("Escriba su nombre de usuario: ")
datos = pd.read_csv(f'Usuarios/{Username}/{Username}.csv', header=0)
# print(datos)
# print("")
Locker = datos['Locker']
print(Locker)
#print(datos.ix[0:1])
print(Locker+1)

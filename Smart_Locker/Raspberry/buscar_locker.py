import pandas as pd

Username = input("Escriba su nombre de usuario: ")
df = pd.read_csv(f'.Datos_usuarios/{Username}.csv', header=0)
# print(datos)
# print("")
Locker = df['Locker']
print(Locker)
#print(datos.ix[0:1])
print(Locker+1)

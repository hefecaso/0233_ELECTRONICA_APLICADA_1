import pandas as pd
import time

Username = input("Escriba el nombre del usuario: ")
print(" ")
df = pd.read_csv(f'.Datos_usuarios/{Username}.csv', header=0)
print(df)
time.sleep(30)

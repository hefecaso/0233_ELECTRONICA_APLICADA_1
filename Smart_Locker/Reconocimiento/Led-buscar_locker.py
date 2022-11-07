import RPi.GPIO as GPIO
import time
import pandas as pd

Username = input("Escriba su nombre de usuario: ")
df = pd.read_csv(f'.Datos_usuarios/{Username}.csv', header=0)
# print(datos)
# print("")
Locker = df['Locker']

ESPERA = 0.5
PIN = Locker
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(ESPERA)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(ESPERA)



print("Número de pin activado: ", Locker)

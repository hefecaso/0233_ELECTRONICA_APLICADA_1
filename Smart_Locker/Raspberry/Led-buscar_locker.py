import RPi.GPIO as GPIO
import time
import pandas as pd
import csv

Casillero = int(input("Escriba su Locker y si el registro biometrico es valido se aperturará "))
#Username = input("digite su nombre para confirmar")
#df = pd.read_csv(f'.Datos_usuarios/{Username}.csv', header=0)

# print(datos)
# print("")
Locker = (Casillero + 3)

ESPERA = 0.5
PIN = Locker
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(ESPERA)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(ESPERA)



print("Número de pin activado: ", Locker)

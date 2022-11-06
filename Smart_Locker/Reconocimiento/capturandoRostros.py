import cv2
import os
import imutils
import time
#########################################
#   Pidiendo nombre para el Usuarios    #
#########################################

import getpass
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

Username = input("Escriba su nombre de usuario: ")
Contraseña = getpass.getpass("Ingrese su contraseña: ")
Locker = int(input("Digite el numero de locker que desea: "))
Dpi = int(input("Digite su numero de identificacion personal: "))
print("Capturando rostro, espere un momento...")
time.sleep(2)
#savetxt("Nombre.csv", array([Nombre,Contraseña,Locker,Dpi]).T , delimiter=",", header='Nombre,Contraseña,Locker,Dpi')



#########################################
personName = Username
dataPath = 'Usuarios'#Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)

cap = cv2.VideoCapture(-1)
#cap = cv2.VideoCapture('Video.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame =  imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
        count = count + 1
    cv2.imshow('frame',frame)

    k =  cv2.waitKey(1)
    if k == 27 or count >= 50:
        break

cap.release()
cv2.destroyAllWindows()

################################################

print("Rostro capturado.")
time.sleep(2)
print(f"Bienvenido {Username}!")
time.sleep(2)

df = pd.DataFrame([[Username,Contraseña,Locker,Dpi]], columns = ['Username', 'Contraseña','Locker', 'Dpi'])
df.to_csv(f'.Datos_usuarios/{Username}.csv')

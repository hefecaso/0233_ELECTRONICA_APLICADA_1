import csv
from os import system
import time

def pass_check():
    Username = False
    Contraseña = False
    username = input("Ingresa el usuario: ")
    file_handle = open(f'.Datos_usuarios/{username}.csv')
    password_check = csv.reader(file_handle)
    counter = 2

    for x in password_check:
        if username == x[1]:
            print("Usuario valido.")
            Nombre = True
            password = input("Ingresa la contraseña: ")
            counter = 2
            while counter > 0:
                if password == x[2]:
                    print("Acceso habilitado")
                    Contraseña = True
                    time.sleep(2)
                    exec(open("Ventana_ingreso_usuario.py").read())
                    return "yes"
                    break
                else:
                    print("Contraseña incorrecta, porfavor intentelo de nuevo o contacte a un administrador.")
                    password = input("Ingrese la contraseña: ")
                    Contraseña = False
                counter -= 1
            break
        else:
            Username = False
    if Username == True and Contraseña == False:
        print("Contraseña incorrecta")

    file_handle.close()
pass_check()

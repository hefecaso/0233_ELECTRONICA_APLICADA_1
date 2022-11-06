import csv

def pass_check():
    Username = False
    Contraseña = False
    file_handle = open(f'.Datos_Usuarios/hefecaso.csv')
    password_check = csv.reader(file_handle)
    username = input("ingresa el usuario: ")
    counter = 2

    for x in password_check:
        while x != username and counter > 0:
            counter -= 1
            username = input("usuario incorrecto, porfavor ingrese el usuario correcto")
        if username == x[1]:
            print("Usuario valido.")
            Nombre = True
            password = input("ingresa la contraseña: ")
            counter = 2
            while counter > 0:
                if password == x[2]:
                    print("acceso habilitado")
                    Contraseña = True
                    return "yes"
                    break
                else:
                    print("contraseña incorrecta, porfavor intentelo de nuevo")
                    password = input("ingrese la contraseña: ")
                    Contraseña = False
                counter -= 1
            break
        else:
            Username = False
    if Username == True and Contraseña == False:
        print("contraseña incorrecta")

    file_handle.close()
pass_check()

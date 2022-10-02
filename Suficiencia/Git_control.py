from os import system
import os

def menu():
    print('\n##########################')
    print('#    Control de Github   #')
    print('##########################\n')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Git add.")
    print("2. Ver cambios para commit.")
    print("3. Git commit con comentario.")
    print("4. Git push.")
    print("5. Git pull.")
    print("6. Ver historial de commits.")
    print("7. Git reset hard.")
    print("8. Guardando el reset hard.")
    print("9. Ver ramas clonadas y locales.")
    print("10. Clonar ramas a repositorio local.")
    print("11. Cambiando de rama.")
    print("12. Salir.\n")


while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")

    if opc == '1':
        print('=====================================')
        print("git add")
        system(f"git add .")
        print('=====================================')

    elif opc == '2':
        print('====================================================================')
        print("Mostrando cambios para commit")
        system(f"git status")
        print('====================================================================')


    elif opc == '3':
        print('====================================================================')
        print("Git commit con comentario\n")
        comentario = input("Ingrese su comentario: ")
        system(f'git commit -m "{comentario}"')
        print('====================================================================')


    elif opc == '4':
        print('====================================================================')
        print("Git push")
        system(f"git push")
        print('====================================================================')


    elif opc == '5':
        print('====================================================================')
        print("Git pull")
        system(f"git pull")
        print('====================================================================')


    elif opc == '6':
        print('====================================================================')
        print("Mostrando historial de commits")
        system(f"git log --oneline --decorate")
        print('====================================================================')


    elif opc == '7':
        print('====================================================================')
        print("Git reset hard\n")
        commit = input("Ingrese ID del commit: ")
        system(f"git reset --hard {commit}")
        print('====================================================================')


    elif opc == '8':
        print('====================================================================')
        print("Git reset hard\n")
        system(f"git push -f origin")
        print('====================================================================')


    elif opc == '9':
        print('====================================================================')
        print("Mostrando ramas")
        system(f"git branch")
        print('====================================================================')


    elif opc == '10':
        print('====================================================================')
        print("Clonando rama a repositorio local\n")
        system(f"git branch -a")
        rama = input('\nSeleccione la rama que desea clonar: ')
        system(f"git checkout -b {rama} Origin/{rama}")
        print('\nRama clonada!\n')
        system(f"git branch")
        print('====================================================================')


    elif opc == '11':
        print('====================================================================')
        print("Mostrando ramas disponibles\n")
        system(f"git branch")
        rama = input('\nSeleccione la rama que desea: ')
        system(f"git checkout {rama}")
        print(f'\nRama actual {rama}!\n')
        system(f"git branch")
        print('====================================================================')


    elif opc == '12':
        print('====================================================================')
        print("Saliendo del programa.")
        print('====================================================================')
        break


    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")

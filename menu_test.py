from menu import Menu
import os 

TITLE1 = """                                                                                                              
█████▄ ██ █████▄ ██     ██ ▄████▄ ██████ ██████ ▄█████ ▄████▄ 
██▄▄██ ██ ██▄▄██ ██     ██ ██  ██   ██   ██▄▄   ██     ██▄▄██ 
██▄▄█▀ ██ ██▄▄█▀ ██████ ██ ▀████▀   ██   ██▄▄▄▄ ▀█████ ██  ██ 
                                                              
"""
mainMenu = Menu(title=TITLE1)

ls = os.listdir('.')
print(ls)
for file in ls:
    if(file.__contains__('.xml')):
        print("Se encontro el fichero "+file)
        print("[0] Usar "+file)
        print("[1] Crear un nuevo xml")
        opcion = int(input("Seleccione una opción: "))
        if (opcion == 0):
            print("nosequepasa")
        elif (opcion == 1):
            print("No sé que pasa tampoco")
        else:
            print("Eres bobo o k? solo hay dos opciones")

mainMenu.show_windows_menu()

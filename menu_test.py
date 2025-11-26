from menu import menu
import os
import msvcrt
from sys import platform


title1 = """                                                                                                              
█████▄ ██ █████▄ ██     ██ ▄████▄ ██████ ██████ ▄█████ ▄████▄ 
██▄▄██ ██ ██▄▄██ ██     ██ ██  ██   ██   ██▄▄   ██     ██▄▄██ 
██▄▄█▀ ██ ██▄▄█▀ ██████ ██ ▀████▀   ██   ██▄▄▄▄ ▀█████ ██  ██ 
                                                              
"""
mainMenu = menu(title=title1)
mainMenu.selectSubMenu()
#SOLO FUNCIONA EN WINDOWS
if (platform == "win32"):
    opciones = ["Opción 1", "Opción 2", "Opción 3", "Salir"]
    seleccion = 0

    while True:
         # Mostrar menú
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                print(f"> {opcion}")  # resaltado
            else:
                print(f"  {opcion}")

         # Leer tecla
        tecla = msvcrt.getch()

        if tecla == b'H':  # Flecha arriba
            seleccion = (seleccion - 1) % len(opciones)
        elif tecla == b'P':  # Flecha abajo
            seleccion = (seleccion + 1) % len(opciones)
        elif tecla == b'\r':  # Enter
            print(f"Has elegido: {opciones[seleccion]}")
            if opciones[seleccion] == "Salir":
                break
            break

         # Limpiar pantalla para redibujar

        os.system("cls")
else:
    mainMenu.show()
    mainMenu.selectSubMenu()


from menu import menu


title1 = """                                                                                                              
█████▄ ██ █████▄ ██     ██ ▄████▄ ██████ ██████ ▄█████ ▄████▄ 
██▄▄██ ██ ██▄▄██ ██     ██ ██  ██   ██   ██▄▄   ██     ██▄▄██ 
██▄▄█▀ ██ ██▄▄█▀ ██████ ██ ▀████▀   ██   ██▄▄▄▄ ▀█████ ██  ██ 
                                                              
"""
mainMenu = menu(title=title1)

mainMenu.show()
mainMenu.selectSubMenu(2)


#SOLO FUNCIONA EN WINDOWS
# import msvcrt

# opciones = ["Opción 1", "Opción 2", "Opción 3", "Salir"]
# seleccion = 0

# while True:
#     # Mostrar menú
#     for i, opcion in enumerate(opciones):
#         if i == seleccion:
#             print(f"> {opcion}")  # resaltado
#         else:
#             print(f"  {opcion}")

#     # Leer tecla
#     tecla = msvcrt.getch()

#     if tecla == b'H':  # Flecha arriba
#         seleccion = (seleccion - 1) % len(opciones)
#     elif tecla == b'P':  # Flecha abajo
#         seleccion = (seleccion + 1) % len(opciones)
#     elif tecla == b'\r':  # Enter
#         print(f"Has elegido: {opciones[seleccion]}")
#         if opciones[seleccion] == "Salir":
#             break

#     # Limpiar pantalla para redibujar
#     import os
#     os.system("cls")


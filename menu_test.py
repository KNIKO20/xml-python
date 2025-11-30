from menu import Menu
#from god_xml import GodXML
import os 
from sys import platform
if(platform=="win32"):
    import msvcrt

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BG_BLUE = "\033[34m"
BOLD_UNDERLINE = "\033[1;4m"
GRAY = "\x1b[90m"

TITLE1 = """                                                                                                              
█████▄ ██ █████▄ ██     ██ ▄████▄ ██████ ██████ ▄█████ ▄████▄ 
██▄▄██ ██ ██▄▄██ ██     ██ ██  ██   ██   ██▄▄   ██     ██▄▄██ 
██▄▄█▀ ██ ██▄▄█▀ ██████ ██ ▀████▀   ██   ██▄▄▄▄ ▀█████ ██  ██ 
                                                              
"""
mainMenu = Menu(title=TITLE1)


#xml_manager = GodXML()

#available_files = xml_manager.buscar_ficheros('./')
def xml_selector():
    ls = os.listdir('.')
    print(ls)
    xml_files = []
    for file in ls:
        if(file.__contains__('.xml')):
            xml_files.append(file)
    if(len(xml_files) != 0):
        if platform == "":
            opciones = xml_files
            seleccion = 0
            opciones.insert(0, "Crear un nuevo fichero XML")
            opciones.append("Salir")
            while True:
                # Mostrar menú
                print(f"{TITLE1}")
                print(GRAY + "Usa las flechas \u2191 \u2193 para moverte y enter \u23ce para seleccionar" + RESET)
                if(len(xml_files) == 1):
                    print("Se encontro el fichero "+xml_files[0])
                if(len(xml_files) > 1):
                    print("Se encontraron ficheros XML")
                
                for i, opcion in enumerate(opciones):
                    if i == seleccion:
                        print(f"  {GREEN}> {opcion}{RESET}")  # resaltado
                    else:
                        print(f"  {opcion}")

                # Leer tecla
                tecla = msvcrt.getch()

                if tecla == b"H":  # Flecha arriba
                    seleccion = (seleccion - 1) % len(opciones)
                elif tecla == b"P":  # Flecha abajo
                    seleccion = (seleccion + 1) % len(opciones)
                elif tecla == b"\r":  # Enter
                    # print(f"Has elegido: {opciones[seleccion]}")                    
                    if opciones[seleccion] == "Salir":
                        break
                    elif (seleccion == 0):
                        print("Función de crear XML va aquí")
                        break
                    else:
                        """
                        AQUI DEVUELVE EL NOMBRE DEL ARCHIVO
                        """
                        print("Elegiste "+opciones[seleccion])
                        break

                # Limpiar pantalla para redibujar

                os.system("cls")
        else:
            if(len(xml_files) == 1):
                print("Se encontro el fichero "+xml_files[0])
            if(len(xml_files) > 1):
                print("Se encontraron ficheros xml")

            print("[0] Crear un nuevo xml")
            for i,file in enumerate(xml_files):
                print(f"[{i+1}] Usar {file}")

            opcion = int(input("Seleccione una opción: "))
            if (opcion == 0):
                print("Función de crear XML va aquí")
            elif (len(xml_files)+1 > opcion > 0):
                """
                AQUI DEVUELVE EL NOMBRE DEL ARCHIVO
                """
                print(xml_files[opcion-1])
            else:
                print("Eres bobo o k? solo hay dos opciones")
    else:
        print("Función de crear XML va aquí")



xml_selector()

mainMenu.show_windows_menu()



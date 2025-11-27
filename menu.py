from menu_class import option, subMenu
import os
import msvcrt
from sys import platform
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BG_BLUE = "\033[34m"
BOLD_UNDERLINE = "\033[1;4m"

class menu:
    def back(self):
        if (platform == "win32"):
            self.showWindowsMenu()
        else:
            self.showSubMenu()
            self.selectOption(int(input("Selecciona una opcion: ")))


    title: str

    def __init__(self, title):
        self.title = title
        self.elementList = [
        subMenu("Gestion de Usuarios", "/Help",
                [option("Añadir", "/Help", ),
                 option("Mostrar", "/Help", ),
                 option("Eliminar", "/Help", ),
                 option("Busqueda", "/Help", ),
                 option("Salir", "/Help", self.back)]),
        subMenu("Gestion de Libros", "/Help",
                [option("Añadir", "/Help", ),
                 option("Mostrar", "/Help", ),
                 option("Eliminar", "/Help", ),
                 option("Busqueda", "/Help", ),
                 option("Salir", "/Help", self.back)]),
        subMenu("Gestion de Prestamos", "/Help",
                [option("Prestar", "/Help", ),
                 option("Devolver", "/help", ),
                 option("Salir", "/Help", self.back)]
                ),
        subMenu("Salir", "/Help",[])
    ]

    def showSubMenu(self):
        print(self.title)
        for i, element in enumerate(self.elementList):
            print(f"[{i}] {element.nombre}")

    def selectOption(self, numberOption):
        if 3 > numberOption >= 0:
            element = self.elementList[numberOption]
            print("-" * 4 + "[" + element.nombre +"]"+ "-" * 4)
            element.showOptionList()

            numberOptionList = int(input("Selecciones una opción: "))
            optionSelected = element.getOption(numberOptionList)
            optionSelected.execute()
        print("Saliendo...")

    def arraySubMenuOptions(self):
        subMenuArray = []
        for element in self.elementList:
            subMenuArray.append(element.nombre)
        return subMenuArray

    def arrayListOptions(self, subMenuSelected):
        return subMenuSelected.getOption()


    def showWindowsMenu(self):
        if (platform == "win32"):
            opciones = self.arraySubMenuOptions()
            seleccion = 0

            while True:
                # Mostrar menú
                print(f"{self.title}")
                print(f"Usa las flechas para moverte y enter para seleccionar")
                for i, opcion in enumerate(opciones):
                    if i == seleccion:
                        print(f"  {GREEN}> {opcion}{RESET}")  # resaltado
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
                    self.selectOption(seleccion)
                    if opciones[seleccion] == "Salir":
                        break
                    break

                # Limpiar pantalla para redibujar

                os.system("cls")
        else:
            self.show()
            self.selectOption()



        
    




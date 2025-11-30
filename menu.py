"""Modules imported to detect the user's O.S. and to detect keys (arrows) """

import os
from sys import platform
if(platform=="win32"):
    import msvcrt
from menu_class import Option, SubMenu

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BG_BLUE = "\033[34m"
BOLD_UNDERLINE = "\033[1;4m"
GRAY = "\x1b[90m"


class Menu:
    """Class representing a menu interface."""

    def __init__(self, title):
        self.title = title
        self.element_list = [
            SubMenu(
                "Gestion de Usuarios",
                "/Help",
                [
                    Option(
                        "Añadir",
                        "/Help",
                    ),
                    Option(
                        "Mostrar",
                        "/Help",
                    ),
                    Option(
                        "Eliminar",
                        "/Help",
                    ),
                    Option(
                        "Busqueda",
                        "/Help",
                        self.busqueda
                    ),
                    Option("Salir", "/Help", self.back),
                ],
            ),
            SubMenu(
                "Gestion de Libros",
                "/Help",
                [
                    Option(
                        "Añadir",
                        "/Help",
                    ),
                    Option(
                        "Mostrar",
                        "/Help",
                    ),
                    Option(
                        "Eliminar",
                        "/Help",
                    ),
                    Option(
                        "Busqueda",
                        "/Help",
                        self.busqueda
                    ),
                    Option("Salir", "/Help", self.back),
                ],
            ),
            SubMenu(
                "Gestion de Prestamos",
                "/Help",
                [
                    Option(
                        "Prestar",
                        "/Help",
                    ),
                    Option(
                        "Devolver",
                        "/help",
                    ),
                    Option("Salir", "/Help", self.back),
                ],
            ),
            SubMenu("Salir", "/Help", []),
        ]

    def back(self):
        """
        Function that reloads the main menu
        """
        if platform == "win32":
            self.show_windows_menu()
        else:
            self.show_submenu()
            self.select_option(int(input("Selecciona una opcion: ")))
    
    def busqueda(self):
        print("Buscando...")

    def show_submenu(self):
        """
        Function that prints the available options.
        """
        print(self.title)
        for i, element in enumerate(self.element_list):
            print(f"[{i}] {element.nombre}")

    def select_option(self, number_option):
        """
        Function that displays the list of options from the selected submenu
        and executes the chosen function.

        :param numberOption: index of the chosen option
        """
        if platform == "win32":
            
            seleccion = 0
            element = self.element_list[number_option]
            opciones = self.array_list_options(element)
            while True:
                print(BG_BLUE + "-" * 4 + "[" + RESET + BOLD_UNDERLINE + element.nombre + RESET + BG_BLUE + "]" + "-" * 4 + RESET)
                print(GRAY + "Usa las flechas \u2191 \u2193 para moverte y enter \u23ce para seleccionar" + RESET)
                for i, opcion in enumerate(opciones):
                    if i == seleccion:
                        print(f"  {GREEN}> {opcion}{RESET}")  # resaltado
                    else:
                        print(f"  {opcion}")
                tecla = msvcrt.getch()

                if tecla == b"H":  # Flecha arriba
                    seleccion = (seleccion - 1) % len(opciones)
                elif tecla == b"P":  # Flecha abajo
                    seleccion = (seleccion + 1) % len(opciones)
                elif tecla == b"\r":  # Enter
                    # print(f"Has elegido: {opciones[seleccion]}")                   
                    if opciones[seleccion] == "Salir":
                        self.show_windows_menu()
                    else:
                        option_selected = element.get_option(seleccion)
                        option_selected.execute()
                    break

                # Limpiar pantalla para redibujar

                os.system("cls")
        else:
            if 0 <= number_option <= len(self.element_list):
                element = self.element_list[number_option]
                print("-" * 4 + "[" + element.nombre + "]" + "-" * 4)
                element.show_option_list()

                number_option_list = int(input("Selecciones una opción: "))
                option_selected = element.get_option(number_option_list)
                option_selected.execute()
        self.back

    def array_submenu_options(self):
        """
        Function that returns an array of submenu options for use in other
        functions.
        """
        submenu_array = []
        for element in self.element_list:
            submenu_array.append(element.nombre)
        return submenu_array

    def array_list_options(self, submenu_selected):
        """
        Function that returns an array of options from a given submenu for use
        in other functions.
        """
        options_array = []
        for option in submenu_selected.get_array_options():
            options_array.append(option.get_nombre())
        return options_array

    def show_windows_menu(self):
        """
        Function that displays the Windows-specific menu or the standard menu.
        """
        if platform == "win32":
            opciones = self.array_submenu_options()
            seleccion = 0

            while True:
                # Mostrar menú
                print(f"{self.title}")
                print(GRAY + "Usa las flechas \u2191 \u2193 para moverte y enter \u23ce para seleccionar" + RESET)
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
                    else:
                        self.select_option(seleccion)
                        break

                # Limpiar pantalla para redibujar

                os.system("cls")
        else:
            self.show_submenu()
            option_selected = int(input("Selecciona una opcion: "))
            if(option_selected==len(self.element_list)-1):
                print("Saliendo...")
            else:
                self.select_option(option_selected)

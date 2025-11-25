from menu_class import option, subMenu
import os

class menu:
    title: str
    elementListBase = [
        subMenu("Gestion de Usuarios", "/Help",
                [option("Añadir", "/Help", "Funcion Para Añadir()"),
                 option("Mostrar", "/Help", "Funcion Para Mostrar()"),
                 option("Eliminar", "/Help", "Funcion Para Eliminar()"),
                 option("Busqueda", "/Help", "Funcion Para Busqueda()"),
                 option("Salir", "/Help", "Funcion Para Salir()")]),
        subMenu("Gestion de Libros", "/Help",
                [option("Añadir", "/Help", "Funcion Para Añadir()"),
                 option("Mostrar", "/Help", "Funcion Para Mostrar()"),
                 option("Eliminar", "/Help", "Funcion Para Eliminar()"),
                 option("Busqueda", "/Help", "Funcion Para Busqueda()"),
                 option("Salir", "/Help", "Funcion Para Salir()")]),
        subMenu("Gestion de Prestamos", "/Help",
                [option("Prestar", "/Help", "Funcion Para Cambiar Estado Prestar()"),
                 option("Devolver", "/help", "Funcion Para Cambiar Estado Devolver()"),
                 option("Salir", "/Help", "Funcion Para Salir()")]
                )
    ]
    def __init__(self, title, elementList=elementListBase):
        self.title = title
        self.elementList = elementList
    def show(self):
        print("*"* (len(self.title)+2))
        print("*"+self.title+"*")
        print("*"* (len(self.title)+2))
        for element in self.elementList:
            print("[+] "+element.nombre)
    def selectSubMenu(self,numberOption):
        element = self.elementList[numberOption]
        print("-" * 4 + "[" + element.nombre +"]"+ "-" * 4)
        element.execute()
        #self.elementList = self.elementList[1:]


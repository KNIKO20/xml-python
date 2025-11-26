from numpy.ma.core import append

from menu_class import option, subMenu
import os

class menu:
    def salir(self):
        self.selectSubMenu()


    title: str

    def __init__(self, title):
        self.title = title
        self.elementList = [
        subMenu("Gestion de Usuarios", "/Help",
                [option("Añadir", "/Help", ),
                 option("Mostrar", "/Help", ),
                 option("Eliminar", "/Help", ),
                 option("Busqueda", "/Help", ),
                 option("Salir", "/Help",  self.salir)]),
        subMenu("Gestion de Libros", "/Help",
                [option("Añadir", "/Help", ),
                 option("Mostrar", "/Help", ),
                 option("Eliminar", "/Help", ),
                 option("Busqueda", "/Help", ),
                 option("Salir", "/Help", self.salir)]),
        subMenu("Gestion de Prestamos", "/Help",
                [option("Prestar", "/Help", ),
                 option("Devolver", "/help", ),
                 option("Salir", "/Help")]
                ),
        subMenu("Salir", "/Help",[])
    ]

    option: int
    def showSubMenu(self):
        print(self.title)
        for i, element in enumerate(self.elementList):
            print(f"[{i}] {element.nombre}")
        self.option = int(input("Selecciona una opcion: "))

    def selectSubMenu(self,numberOption=None):
        if numberOption < 2 and numberOption >= 0:
            element = self.elementList[numberOption]
            print("-" * 4 + "[" + element.nombre +"]"+ "-" * 4)
            element.showOptionList()

            numberOptionList = int(input("Selecciones una opción: "))
            optionSelected = element.getOption(numberOptionList)
            optionSelected.execute()
        print("Saliendo...")
    def showSubMenuOptions(self):
        subMenuArray = []
        for element in self.elementList:
            subMenuArray.append(element.nombre)
        return subMenuArray



        
    




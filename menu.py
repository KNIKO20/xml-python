from menu_class import option, subMenu

class menu:
    title: str
    elementListBase = [
        subMenu("Gestion de Usuarios", "/Help",
                [option("Añadir", "/Help", "Funcion Para Añadir()"),
                 option("Mostrar", "/Help", "Funcion Para Mostrar()"),
                 option("Eliminar", "/Help", "Funcion Para Eliminar()"),
                 option("Busqueda", "/Help", "Funcion Para Busqueda()")]),
        subMenu("Gestion de Libros", "/Help",
                [option("Añadir", "/Help", "Funcion Para Añadir()"),
                 option("Mostrar", "/Help", "Funcion Para Mostrar()"),
                 option("Eliminar", "/Help", "Funcion Para Eliminar()"),
                 option("Busqueda", "/Help", "Funcion Para Busqueda()")]),
        subMenu("Gestion de Prestamos", "/Help",
                [option("Prestar", "/Help", "Funcion Para Cambiar Estado Prestar()"),
                 option("Devolver", "/help", "Funcion Para Cambiar Estado Devolver()"), ]
                )
    ]
    def __init__(self, title, elementList=elementListBase):
        self.title = title
        self.elementList = elementList
    def show(self):
        print(self.title)
        for element in self.elementList:
            print(element.nombre)
    def select(self):
        element = self.elementList[0]
        element.execute()
        #self.elementList = self.elementList[1:]


class ElementMenu:
    """
    Base class representing a generic menu element.
    """
    nombre: str
    descripcion: str

    def __init__(self, paramNombre, paramDescripcion):
        """
        Initialize an ElementMenu instance.

        Args:
            paramNombre (str): The name of the element.
            paramDescripcion (str): The description of the element.
        """
        self.nombre = paramNombre
        self.descripcion = paramDescripcion

    def get_nombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion


class Option(ElementMenu):
    """
    Represents a selectable option in a menu.

    Inherits from ElementMenu and adds an executable function.
    """
    def __init__(self, paramNombre, paramDescripcion, funct=None):
        super().__init__(paramNombre, paramDescripcion)
        self.funcion = funct

    def execute(self):
        self.funcion()


class SubMenu(ElementMenu):
    """
    Represents a submenu containing multiple options.

    Inherits from ElementMenu and manages a list of Option objects.
    """
    option_list: list

    def __init__(self, paramNombre, paramDescripcion, paramOptions=None,
                 funct=None):
        super().__init__(paramNombre, paramDescripcion)
        self.option_list = paramOptions
        self.funct = funct

    def show_option_list(self):
        for i, option_element in enumerate(self.option_list):
            print(f"[{i}] {option_element.get_nombre()}")

    def get_option(self):
        return self.option_list

    def execute(self):
        self.funct()



class elementMenu:
    nombre: str
    descripcion: str
    def __init__(self, paramNombre, paramDescripcion):
        self.nombre = paramNombre
        self.descripcion = paramDescripcion

    def getNombre(self):
        return self.nombre
    def getDescripcion(self):
        return self.descripcion

class option(elementMenu):

    def __init__(self, paramNombre, paramDescripcion, funct=None):
        super().__init__(paramNombre, paramDescripcion)
        self.funcion = funct
    def execute(self):
        self.funcion()

class subMenu(elementMenu):
    optionList: list
    def __init__(self, paramNombre, paramDescripcion, paramOptions=None, funct=None):
        super().__init__(paramNombre, paramDescripcion)
        self.optionList = paramOptions
        self.funct = funct

    def showOptionList(self):
        for i,optionElement in enumerate(self.optionList) :
            print(f"[{i}] {optionElement.getNombre()}")

    def getOption(self, numberOption):
        return self.optionList[numberOption]
    def execute(self):
        self.funct()


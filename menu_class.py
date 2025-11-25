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
    def execute(self):
        print(self.nombre, self.descripcion)
class option(elementMenu):
    accion: str
    def __init__(self, paramNombre, paramDescripcion, paramAccion):
        super().__init__(paramNombre, paramDescripcion)
        self.accion = paramAccion
    def execute(self):
        print(self.accion)
class subMenu(elementMenu):
    optionList: list
    def __init__(self, paramNombre, paramDescripcion, paramOptions):
        super().__init__(paramNombre, paramDescripcion)
        self.optionList = paramOptions
    def showOptionList(self):
        for optionElement in self.optionList:
            print("> "+optionElement.getNombre())
    def getOption(self, numberOption):
        return self.optionList[numberOption]



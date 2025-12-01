import xml.etree.ElementTree as ET


class GodXML():
    fichero: ET.ElementTree = None
    root: ET.Element = None

    def __init__(self, ):
        pass

    def buscar_ficheros(self, workdir: str):
        import os
        with os.scandir(workdir) as ficheros:
            return [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.xml')]

    #  Este metodo carga un fichero en la instancia de GodXML.
    def cargar_fichero(self, nombre: str ):
        # try: 
        self.filename = nombre #NOMBRE DEL FICHERO para ponerlo en el write al guardar cambios
        self.fichero = ET.parse(nombre)
        self.root = self.fichero.getroot() #Porque se necesitará para añadir/borrar/modificar

        # except Exception as e:
        #     print(e)

    
    def anyadir_elemento(self, parentName: str, childName:str, text_del_Elemento: str, attributes = dict ({})):
        # try:
        if parentName is not None:
    
            parentElement = self.root.find(parentName)
            
            childElement = ET.SubElement(parentElement, childName)
            
           
        else:
            childElement=ET.SubElement (self.root, childName)

        childElement.attrib= attributes
        childElement.text = text_del_Elemento
        # except Exception as e:
        #     print(e)

    def guardar_cambios (self):
        tree = ET.ElementTree(self.root)
        tree.write(self.filename, encoding="utf-8", xml_declaration=True)


    def eliminar_elemento(self, elementPath: str):

        parent_map = {child: parent for parent in self.root.iter() for child in parent}

        for el in self.root.findall(elementPath):
            print(el)
            parent_map[el].remove(el)
    



    
    


        

def añadir_elemento(parentName: str = None, childName: str = ''):
    # TODO: Borrar esta parte que caraga el XML, porque deberia estar en otra funcion.
    fichero = ET.parse('nombre.xml')

    # Asumimos que cada vez que el archivo sea seleccionado para añadir simpre va a tener un root que es el padre de todos.
    root = fichero.getroot()


    if parentName is not None:
        parentElement = root.find(parentName)
        childElement = ET.SubElement(parentElement, childName)

    
    
    
    tree = ET.ElementTree(root)
    tree.write('nombre.xml', encoding="utf-8", xml_declaration=True)

# añadir_elemento('libros', 'libro')


xml_jonathan= GodXML() #INSTANCIa la CLASE
xml_jonathan.cargar_fichero('nombre copy.xml')
# xml_jonathan.anyadir_elemento(None , 'libros', None)
# xml_jonathan.anyadir_elemento('libros', 'libro','COMIDA', ) #Chicos al llamar a este método, recuerden meter dicionarios en el atributo; si no dejenlo vacío (SIN NONE)
xml_jonathan.eliminar_elemento('libros/libro')
xml_jonathan.guardar_cambios ()


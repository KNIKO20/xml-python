import xml.etree.ElementTree as ET
from datetime import datetime


class GodXML():
    def __init__(self):
        self.fichero: ET.ElementTree = None
        self.root: ET.Element = None
        self.filename: str = None

    def buscar_ficheros(self, workdir: str):
        import os
        with os.scandir(workdir) as ficheros:
            return [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.xml')]
        
    def init_fichero(self):
        
        self.root = ET.Element('biblioteca')
        ET.SubElement(self.root, 'libros')
        ET.SubElement(self.root, 'usuarios')
        ET.SubElement(self.root, 'prestamos')

        self.filename = 'Biblioteca_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.xml'

    #  Este metodo carga un fichero en la instancia de GodXML.
    def cargar_fichero(self, nombre: str ):
        # try: 
        self.filename = nombre #NOMBRE DEL FICHERO para ponerlo en el write al guardar cambios
        self.fichero = ET.parse(nombre)
        self.root = self.fichero.getroot() #Porque se necesitará para añadir/borrar/modificar

        # except Exception as e:
        #     print(e)
        
    def anyadir_elemento(self, parentName: str, childName:str, text_del_Elemento: str, attributes = dict ({})): #Aquí quieres pasar 'libro', 'nombre', 'textonombre', 'atributosNombre', nuevoelemento (en este caso autor), nombre, atributos (si tuviese) (etc todo en una linea?????)
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

    def modificar_elemento (self, texto_del_Elem :str, identificador: str, nombre_atr: str, nuevo_nombre_atr: str, nuevo_nombre_elem: str ): #nO RECUERDO POR QUÉ PUSE RUTA

        #Primero se pide el id.
        #Después, se busca ese id en todos los nombres y atributos
        for elemento in self.root.iter():
            print(elemento)
            if elemento.attrib.get("id") == identificador: #Para saber el id. #Dentro de attrib, que devuelve dic de atrib, coges el id, te devuelve el nombre del id

                    print (elemento.attrib.get("id"))
                    #JURARÍA QUE TENGO QUE PREGUNTAR SI QUIERE CAMBIAR EL TXT DE ESA ETIQUETA O LA ETIQUETA EN SÍ, o el atributo
                    elemento.text= texto_del_Elem #Esto cuidado, no es un método (), son variables =....
                    elemento.set(nombre_atr, nuevo_nombre_atr) #Esto sería para cambiar el atributo, no funciona con el nombre del elemento...
                    elemento.tag = nuevo_nombre_elem

        #Al encontrarlo, tienes que guardar el child.name, y recorrerlo
        #Preguntar qué (de los subhijos) quiere modificar.

    def eliminar_elemento(self, xpath: str):
        """Elimina un elemento del XML usando xpath"""
        elemento = self.root.find(xpath)
        if elemento is not None:
            parent = self.root.find(xpath.rsplit('/', 1)[0])
            if parent is not None:
                parent.remove(elemento)
                return True
        return False
        
        
    

    
    


        

# def añadir_elemento(parentName: str = None, childName: str = ''):
#     # TODO: Borrar esta parte que caraga el XML, porque deberia estar en otra funcion.
#     fichero = ET.parse('nombre.xml')

#     # Asumimos que cada vez que el archivo sea seleccionado para añadir simpre va a tener un root que es el padre de todos.
#     root = fichero.getroot()


#     if parentName is not None:
#         parentElement = root.find(parentName)
#         childElement = ET.SubElement(parentElement, childName)

    
    
    
#     tree = ET.ElementTree(root)
#     tree.write('nombre.xml', encoding="utf-8", xml_declaration=True)

# añadir_elemento('libros', 'libro')


# xml_jonathan= GodXML() #INSTANCIa la CLASE
# xml_jonathan.cargar_fichero('nombre.xml')



#xml_jonathan.anyadir_elemento(None , 'libros', None)
#xml_jonathan.anyadir_elemento('libros', 'librito','ñamñam' ) #Chicos al llamar a este método, recuerden meter dicionarios en el atributo; si no dejenlo vacío (SIN NONE)




# xml_jonathan.anyadir_elemento(None, 'usuarios', None)
# atributos= {'id': 'ñamñam'}
# xml_jonathan.anyadir_elemento('usuarios', 'user', None, atributos)

# xml_jonathan.anyadir_elemento('usuarios/user', 'name', 'Andrea')
# xml_jonathan.anyadir_elemento('usuarios/user', 'apellidos', 'Dev' )
# xml_jonathan.anyadir_elemento('usuarios/user', 'correo', 'yupiii, funciona:)' )
# xml_jonathan.anyadir_elemento('usuarios/user', 'fechaNacimiento', '28/12/2001' )




# xml_jonathan.guardar_cambios ()
# xml_jonathan.eliminar_elemento('lixbro')


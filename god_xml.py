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

    def buscar_contenedor(self, xpath: str):
        """
        Busca y retorna un contenedor/elemento usando xpath.

        Args:
            xpath: Ruta del elemento a buscar (ej: 'libros', 'usuarios/user')

        Returns:
            Elemento encontrado o None
        """
        return self.root.find(xpath)

    def buscar_todos_hijos(self, parent_xpath: str, tag: str):
        """
        Busca todos los elementos hijos con un tag específico.

        Args:
            parent_xpath: Ruta del elemento padre
            tag: Tag de los elementos a buscar

        Returns:
            Lista de elementos encontrados
        """
        parent = self.root.find(parent_xpath) if parent_xpath else self.root
        if parent is not None:
            return parent.findall(tag)
        return []

    def crear_elemento_con_hijos(self, parent_xpath: str, tag: str, atributos: dict, hijos: dict):
        """
        Crea un elemento con atributos y elementos hijos.

        Args:
            parent_xpath: Ruta del elemento padre donde se creará el nuevo elemento
            tag: Tag del nuevo elemento
            atributos: Diccionario con atributos del elemento
            hijos: Diccionario {tag: texto} con los elementos hijos a crear

        Returns:
            El elemento creado
        """
        parent = self.root.find(parent_xpath) if parent_xpath else self.root
        if parent is None:
            return None

        # Crear elemento principal con atributos
        nuevo_elemento = ET.SubElement(parent, tag, atributos)

        # Agregar elementos hijos
        for hijo_tag, hijo_texto in hijos.items():
            hijo = ET.SubElement(nuevo_elemento, hijo_tag)
            hijo.text = hijo_texto

        return nuevo_elemento

    def obtener_texto_elemento(self, elemento, tag: str):
        """
        Obtiene el texto de un elemento hijo.

        Args:
            elemento: Elemento padre
            tag: Tag del elemento hijo

        Returns:
            Texto del elemento o None
        """
        hijo = elemento.find(tag)
        return hijo.text if hijo is not None else None

    def obtener_atributo(self, elemento, nombre_atributo: str, default=''):
        """
        Obtiene el valor de un atributo de un elemento.

        Args:
            elemento: Elemento del cual obtener el atributo
            nombre_atributo: Nombre del atributo
            default: Valor por defecto si no existe

        Returns:
            Valor del atributo
        """
        return elemento.attrib.get(nombre_atributo, default)

    def eliminar_hijo(self, parent_xpath: str, child_element):
        """
        Elimina un elemento hijo de un padre.

        Args:
            parent_xpath: Ruta del elemento padre
            child_element: Elemento hijo a eliminar

        Returns:
            True si se eliminó, False si no
        """
        parent = self.root.find(parent_xpath) if parent_xpath else self.root
        if parent is not None:
            try:
                parent.remove(child_element)
                return True
            except ValueError:
                return False
        return False

    def contar_elementos(self, parent_xpath: str, tag: str):
        """
        Cuenta cuántos elementos con un tag específico existen en un padre.

        Args:
            parent_xpath: Ruta del elemento padre
            tag: Tag de los elementos a contar

        Returns:
            Cantidad de elementos
        """
        elementos = self.buscar_todos_hijos(parent_xpath, tag)
        return len(elementos)

    def crear_elemento_solo_atributos(self, parent_xpath: str, tag: str, atributos: dict):
        """
        Crea un elemento con solo atributos, sin elementos hijos.

        Args:
            parent_xpath: Ruta del elemento padre donde se creará el nuevo elemento
            tag: Tag del nuevo elemento
            atributos: Diccionario con atributos del elemento

        Returns:
            El elemento creado o None si falla
        """
        parent = self.root.find(parent_xpath) if parent_xpath else self.root
        if parent is None:
            return None

        nuevo_elemento = ET.SubElement(parent, tag, atributos)
        return nuevo_elemento

    def buscar_elemento_por_atributo(self, parent_xpath: str, tag: str, nombre_atributo: str, valor_atributo: str):
        """
        Busca un elemento por el valor de un atributo.

        Args:
            parent_xpath: Ruta del elemento padre donde buscar
            tag: Tag de los elementos a buscar
            nombre_atributo: Nombre del atributo
            valor_atributo: Valor del atributo a buscar

        Returns:
            Elemento encontrado o None
        """
        elementos = self.buscar_todos_hijos(parent_xpath, tag)
        for elemento in elementos:
            if elemento.attrib.get(nombre_atributo) == valor_atributo:
                return elemento
        return None

    def modificar_texto_elemento(self, elemento, tag: str, nuevo_texto: str):
        """
        Modifica el texto de un elemento hijo.

        Args:
            elemento: Elemento padre
            tag: Tag del elemento hijo a modificar
            nuevo_texto: Nuevo texto para el elemento

        Returns:
            True si se modificó, False si no
        """
        hijo = elemento.find(tag)
        if hijo is not None:
            hijo.text = nuevo_texto
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


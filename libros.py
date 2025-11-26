#  2 GESTION LIBROS:
                # AÑADIR
                # MOSTRAR
                # ELIMINAR
                # BUSQUEDA
 
 # Para obtener el elemento raíz del documento, se utiliza el método getroot():

# raiz = doc.getroot()
# print(raiz.tag)               
     
#ORDEN DE EJECUCION:
    #Primero eneseñar un"menu" donde tenga: preguntará al usuario si quiere añadir, mostrar información
        #[Cualquier acción que implique una búsqueda deberá devolver todas las opciones posibles, imprimiendo en pantalla estas mismas y dando a elegir que elemento debe seleccionar]
    # o eliminar a un libro del catálogo.
    # Segundo, al elegir la opcion ejecutar la funcion respectiva de esa opcion
    # Tercero, los cambios que haga deben guardarse en el archivo XML elegido.
    # Cuarto, al sacar informacion, hacer que los datos salgan por la consola en un formato adecuado, y no con el formato de etiquetas.
    
# Para las funciones respectivas a cada opcion del menu, necesito importar las librerias necesarias para ello.
# Ademas, se debe establecer el formato con el que saldran los datos por la terminal. 
# Búsqueda y selección

# 


import xml.etree.ElementTree as ET
tree = ET.parse('AQUI VA LA RUTA DEL DOCUEMENTO XML')
root = tree.getRoot()
for elem in root:
    print(elem.tag, elem.text)#abrir archivo y mostar datos 

### Create XML element tree

root = ET.Element("Person", {"id": "123"})#con atributos
name = ET.SubElement(root, "Name")
name.text = "John"
age = ET.SubElement(root, "Age")
age.text = "30"

### Write XML element tree to file

tree = ET.ElementTree(root)
tree.write("person.xml", encoding="utf-8", xml_declaration=True) # Formateo customizado 






























def menu():
    return

def showInfo():#formato -> {ID: 001 | Título: El Quijote | Autor: Cervantes | Disponible: Sí/No}
    return

def searchInfo():# Si el usuario busca por título o autor, listar todas las coincidencias. 
    return


def choose():# Permitir elegir el libro exacto por ID.  
    return



def addInfo():
    return

def deleteInfo():
    return

def saveInfo(): #El fichero XML deberá guardar la estructura definida en el XML Schema.
    return

 
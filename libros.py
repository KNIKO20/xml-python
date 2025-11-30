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

Modificando un archivo XML
ElementTree proporciona una forma sencilla de construir documentos XML y escribirlos en archivos. El método ElementTree.write() sirve para este propósito.

Una vez creado, un objeto Element puede ser manipulado cambiando directamente sus campos (como Element.text), añadiendo y modificando atributos (método Element.set()), así como añadiendo nuevos hijos (por ejemplo con Element.append()).

Digamos que queremos añadir uno al rango de cada país, y añadir un atributo updated al elemento rango:

Copy
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output.xml')






def menu():
    match opcion:
        case 1:
            addInfo()
        
        case 2:
            showInfo()
            
        case 3:
            deleteInfo()
            
        case 4:
            searchInfo()
        
        
        
        
        
        


import xml.etree.ElementTree as ET

# Crear un elemento raíz
root = ET.Element("biblioteca")

# Crear un hijo
libro = ET.Element("libro")
libro.set("id", "1")

# Añadir un subelemento al hijo
titulo = ET.Element("titulo")
titulo.text = "El Quijote"

# 👉 Añadir el subelemento 'titulo' al elemento 'libro'
libro.append(titulo)

# 👉 Añadir el hijo 'libro' al elemento raíz
root.append(libro)

# Convertir a string para ver el resultado
tree = ET.ElementTree(root)
ET.dump(tree)


def addInfo():#Los libros tienen: nombre, autor y fecha de publicacion(tipo:date)
    root = ET.Element("biblioteca")
    libro = ET.Element("libro")
    libro.set()
    #Añado el tiutlo del libro
    nombre = ET.Element("nombre")
    nombre.text = input("Escriba el título del libro: ")
    
    #Añado autor del libro
    autor = ET.Element("autor")
    autor.text = input("Escriba el autor del libro: ")
    
    fechaPublicacion = ET.Element("fechaPublicacion")
    fechaPublicacion.text = input("Escriba la fecha de publicación del libro (YYYY-MM-DD): ")
    
    #Añado elementos hijo a "libro", y libro a "biblioteca"
    
    root.append(libro)#meto libro
    libro.append(nombre) # meto nombre
    libro.append(autor) #meto autor
    libro.append(fechaPublicacion) # meto fecha



def showInfo():#formato -> {ID: 001 | Título: El Quijote | Autor: Cervantes | Disponible: Sí/No}
    # Parsear el archivo
    tree = ET.parse('AQUI VA LA RUTA DEL DOCUEMENTO XML')
    root = tree.getRoot() 
    
    for libro in root.findall("libro"):
        print("ID:",libro.attrib["id"],"| Título: ",libro.find("nombre").text," | Autor: ",libro.find("autor").text,
        "| Fecha de Publicación: ",libro.find("fechaPublicacion").text," Disponible: Sí/No")#
        print("-"*25)
        

def searchInfo():# Si el usuario busca por título o autor, listar todas las coincidencias. 
    search = input("¿Qué desea buscar?: ")
    for libro in root.findall("libro"):
        autor = libro.find("autor").text
        titulo = libro.find("titulo").text
        
        if autor==search or titulo==search:
            print("Coincidente:")
            print(showInfo)
        


def choose():# Permitir elegir el libro exacto por ID.  
    return




def deleteInfo():#zxPodemos eliminar elementos utilizando Element.remove(). Digamos que queremos eliminar todos los países con un rango superior a 50:

# for country in root.findall('country'):
#     # using root.findall() to avoid removal during traversal
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)

# tree.write('output.xml')
# Tenga en cuenta que la modificación concurrente mientras se itera puede conducir a problemas, al igual que cuando se itera y modifica listas o diccionarios de Python. Por lo tanto, el ejemplo recoge primero todos los elementos coincidentes con root.findall(), y sólo entonces itera sobre la lista de coincidencias.
     return


def saveInfo(): #El fichero XML deberá guardar la estructura definida en el XML Schema.
    return

 
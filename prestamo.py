            # 3 GESTION PRESTAMOS:
                # PRESTAMO: 
                # DEVOLUCION:
                
                
# 1. IMPORTAR LIBRERIAS

# 2. FORMATO

# 3. BUSQUEDA Y SELECCION

# 4. GUARDAR CAMBIOS

import xml.etree.ElementTree as ET
tree = ET.parse('AQUI VA LA RUTA DEL DOCUMENTO XML')
root = tree.getroot()
for elem in root:
    print(elem.tag, elem.text)# abrir y leer elementos del XML

def prestarLibro():
    return

def devolucionLibro():
    return

def saveInfo(): #El fichero XML deberá guardar la estructura definida en el XML Schema.
    return

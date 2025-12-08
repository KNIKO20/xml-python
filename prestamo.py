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
while True:
    print("¿Qué tramite desea realizar?")
    print("1. Préstamo")
    print("2. Devolución")
    print("0. SALIR")
    opcion = input()
    match opcion:
        case "1":
            prestarLibro()
       
        case "2":
            devolucionLibro()
            
        case "0":
            print("SALIENDO.")
            break
        
        case _: 
            print("Valor no válido.")
            
    
    
    
    
    
    

def prestarLibro():
    #1. que libro quiero prestar
    #2. disponibilidad? si=prestar; no=no se puede, elegir otro
    #3. para prestarlo: asociar el id-usuario al atributo 'usuario de prestamo'
        #3.1 añadir usuario al atributo de libro
    return

def devolucionLibro():
    return

def saveInfo(): #El fichero XML deberá guardar la estructura definida en el XML Schema.
    return

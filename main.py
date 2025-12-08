from menu import Menu
from god_xml import GodXML
from user_manager import UserManager
from libros import LibroManager
from prestamo import PrestamoManager

# main function
    # ver si hay un XML en la carpeta de trabajo.
    # Preguntar si queremos usar el existente.

        # Usar el ya creado (XML):
            #  usar XML

        # Un nuevo XML:  
            # Hacer preguntas para crear el XML (libros y usarios)
        
            # Bucle libros:
                # nombre: string
                # autor: string
                # fechaPublicacion: string YYYY-MM-DD
                # id (creado por nosotro como atributo)

            # Bucle usuarios:
                # nombre: string
                # apellidos: string
                # correo: string
                # fechaNacimiento: string YYYY-MM-DD
                # id (creado por nosotro como atributo)
            
            # Preguntar si hay prestamos o no.
            # Bucle prestamo:
                # id (creado por nosotro como atributo)
                # usuario (id del usuario como atributo)
    
        # mostrar menu:
            # 1 GESTION USUARIOS:
                # AÑADIR: lo que añadio.
                # MOSTRAR: un solo registro.
                # ELIMINAR: el eliminado.
                # BUSQUEDA: una lista de registros.
            # 2 GESTION LIBROS:
                # AÑADIR
                # MOSTRAR
                # ELIMINAR
                # BUSQUEDA
            # 3 GESTION PRESTAMOS:
                # PRESTAMO: 
                # DEVOLUCION:

# creo que vamos hacer mas eficientes si cada
# uno se adjudica una funcion del packete xml


if __name__ == "__main__" :

    xml_manager = GodXML()
    available_files = xml_manager.buscar_ficheros('./')
    
    available_files.insert(0,'NUEVO FICHERO')
    available_files_len = len(available_files)
    opcion = 0

    if available_files_len > 1:
        print('Encontramos los siguientes ficheros xml, disponibles, quieres elegir uno: ')
        
        for i in range(available_files_len):
            print((' ' * 5) + f'[{i}] ' + available_files[i])

        opcion = int(input("Seleccione una opción: "))
    

    if opcion > 0:
        xml_manager.cargar_fichero(available_files[opcion])
    else:
        xml_manager.init_fichero()
        xml_manager.guardar_cambios()


    TITLE1 = f"""                                                                                                              
        █████▄ ██ █████▄ ██     ██ ▄████▄ ██████ ██████ ▄█████ ▄████▄ 
        ██▄▄██ ██ ██▄▄██ ██     ██ ██  ██   ██   ██▄▄   ██     ██▄▄██ 
        ██▄▄█▀ ██ ██▄▄█▀ ██████ ██ ▀████▀   ██   ██▄▄▄▄ ▀█████ ██  ██
        Fichero {xml_manager.filename} {'Nuevo archivo' if opcion == 0 else ''}
    """

    user_manager = UserManager(xml=xml_manager)
    libro_manager = LibroManager(xml=xml_manager)
    prestamo_manager = PrestamoManager(xml=xml_manager)

    mainMenu = Menu(title=TITLE1, user_manager=user_manager, libro_manager=libro_manager, prestamo_manager=prestamo_manager)

    mainMenu.show_windows_menu()

    print("+"*20)
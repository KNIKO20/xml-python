from borrow_manager import BorrowManager

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


if __name__ == "__main__" :

    cmd = input('ingresa un numero: ')

    print("+"*20)
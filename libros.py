from god_xml import GodXML


class LibroManager:
    """
    Clase para gestionar libros en el sistema de biblioteca.
    Usa GodXML como dependencia para manipulación XML.
    """

    def __init__(self, xml: GodXML):
        self.xml_manager = xml

    def addInfo(self):
        """
        Añade un nuevo libro al catálogo.
        Los libros tienen: nombre, autor y fecha de publicación
        """
        if self.xml_manager.root is None:
            print("Error: No hay ningún fichero cargado.")
            return

        # Obtener datos del libro
        nombre = input("Escriba el título del libro: ")
        autor = input("Escriba el autor del libro: ")
        fechaPublicacion = input("Escriba la fecha de publicación del libro (YYYY-MM-DD): ")

        # Verificar que existe el contenedor de libros
        libros_container = self.xml_manager.buscar_contenedor('libros')
        if libros_container is None:
            print("Error: No se encontró el contenedor 'libros' en el XML.")
            return

        # Generar ID único para el libro
        cantidad_libros = self.xml_manager.contar_elementos('libros', 'libro')
        nuevo_id = str(cantidad_libros + 1).zfill(3)  # ID con formato 001, 002, etc.

        # Crear el elemento libro con sus hijos
        atributos = {'id': nuevo_id}
        hijos = {
            'nombre': nombre,
            'autor': autor,
            'fechaPublicacion': fechaPublicacion
        }

        self.xml_manager.crear_elemento_con_hijos('libros', 'libro', atributos, hijos)

        print(f"\n✓ Libro añadido con éxito (ID: {nuevo_id})")

        # Guardar cambios
        self.xml_manager.guardar_cambios()

    def showInfo(self, libro_elemento=None):
        """
        Muestra información de los libros.
        Formato: {ID: 001 | Título: El Quijote | Autor: Cervantes | Disponible: Sí/No}

        Args:
            libro_elemento: Si se proporciona, muestra solo ese libro. Si no, muestra todos.
        """
        if self.xml_manager.root is None:
            print("Error: No hay ningún fichero cargado.")
            return

        # Verificar que existe el contenedor
        libros_container = self.xml_manager.buscar_contenedor('libros')
        if libros_container is None:
            print("No hay libros en el catálogo.")
            return

        # Si se proporciona un libro específico, mostrar solo ese
        if libro_elemento is not None:
            libros = [libro_elemento]
        else:
            libros = self.xml_manager.buscar_todos_hijos('libros', 'libro')

        if not libros:
            print("No hay libros en el catálogo.")
            return

        print("\n" + "=" * 80)
        for libro in libros:
            libro_id = self.xml_manager.obtener_atributo(libro, 'id', 'N/A')
            nombre_text = self.xml_manager.obtener_texto_elemento(libro, 'nombre') or "N/A"
            autor_text = self.xml_manager.obtener_texto_elemento(libro, 'autor') or "N/A"
            fecha_text = self.xml_manager.obtener_texto_elemento(libro, 'fechaPublicacion') or "N/A"

            print(f"ID: {libro_id} | Título: {nombre_text} | Autor: {autor_text}")
            print(f"Fecha de Publicación: {fecha_text}")
            print("-" * 80)

    def deleteInfo(self):
        """
        Elimina un libro del catálogo.
        Permite buscar por nombre y confirmar antes de eliminar.
        """
        if self.xml_manager.root is None:
            print("Error: No hay ningún fichero cargado.")
            return

        # Verificar que existe el contenedor
        libros_container = self.xml_manager.buscar_contenedor('libros')
        if libros_container is None:
            print("No hay libros en el catálogo.")
            return

        delete_query = input("¿Qué libro quiere eliminar? (Ingrese el título o ID): ")

        # Buscar libros que coincidan
        libros_encontrados = []
        todos_libros = self.xml_manager.buscar_todos_hijos('libros', 'libro')

        for libro in todos_libros:
            nombre_text = self.xml_manager.obtener_texto_elemento(libro, 'nombre')
            libro_id = self.xml_manager.obtener_atributo(libro, 'id', '')

            if nombre_text and (delete_query.lower() in nombre_text.lower() or delete_query == libro_id):
                libros_encontrados.append(libro)

        if not libros_encontrados:
            print("No se encontraron libros con ese criterio.")
            return

        # Si hay múltiples coincidencias, mostrar opciones
        if len(libros_encontrados) > 1:
            print(f"\nSe encontraron {len(libros_encontrados)} libros:")
            for i, libro in enumerate(libros_encontrados, 1):
                print(f"\n{i}.")
                self.showInfo(libro)

            seleccion = input("Seleccione el número del libro a eliminar (0 para cancelar): ")
            try:
                idx = int(seleccion) - 1
                if idx < 0 or idx >= len(libros_encontrados):
                    print("Eliminación cancelada.")
                    return
                libro_a_eliminar = libros_encontrados[idx]
            except ValueError:
                print("Selección inválida.")
                return
        else:
            libro_a_eliminar = libros_encontrados[0]

        # Mostrar libro y confirmar
        print("\nLibro encontrado:")
        self.showInfo(libro_a_eliminar)

        confirmacion = input("\n¿Quieres eliminar este libro? (S/N): ").upper()
        if confirmacion == 'S':
            if self.xml_manager.eliminar_hijo('libros', libro_a_eliminar):
                print("✓ Libro eliminado con éxito.")
                self.xml_manager.guardar_cambios()
            else:
                print("Error al eliminar el libro.")
        else:
            print("Eliminación cancelada.")

    def searchInfo(self):
        """
        Busca libros por título o autor.
        Lista todas las coincidencias y permite elegir por ID.
        """
        if self.xml_manager.root is None:
            print("Error: No hay ningún fichero cargado.")
            return

        # Verificar que existe el contenedor
        libros_container = self.xml_manager.buscar_contenedor('libros')
        if libros_container is None:
            print("No hay libros en el catálogo.")
            return

        search_query = input("¿Qué desea buscar? (título o autor): ").lower()

        resultados = []
        todos_libros = self.xml_manager.buscar_todos_hijos('libros', 'libro')

        for libro in todos_libros:
            nombre_text = self.xml_manager.obtener_texto_elemento(libro, 'nombre')
            autor_text = self.xml_manager.obtener_texto_elemento(libro, 'autor')

            nombre_lower = nombre_text.lower() if nombre_text else ""
            autor_lower = autor_text.lower() if autor_text else ""

            if search_query in nombre_lower or search_query in autor_lower:
                resultados.append(libro)

        if not resultados:
            print("No se encontraron coincidencias.")
            return

        print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
        for libro in resultados:
            self.showInfo(libro)

        # Permitir elegir por ID
        elegir = input("\n¿Desea ver detalles de un libro específico? (Ingrese ID o Enter para salir): ")
        if elegir:
            for libro in resultados:
                if self.xml_manager.obtener_atributo(libro, 'id') == elegir:
                    print("\nDetalles del libro seleccionado:")
                    self.showInfo(libro)
                    return
            print("ID no encontrado en los resultados.")



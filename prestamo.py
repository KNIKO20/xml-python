from god_xml import GodXML


class PrestamoManager:
    """
    Clase para gestionar préstamos en el sistema de biblioteca.
    Usa GodXML como dependencia para manipulación XML.
    """

    def __init__(self, xml: GodXML):
        self.xml_manager = xml

    def prestar(self):
        """
        Crea un registro de préstamo.
        Requiere: ID de libro disponible e ID de usuario existente.
        """
        if self.xml_manager.root is None:
            print("Error: No hay ningún fichero cargado.")
            return

        # Verificar que existen los contenedores
        libros_container = self.xml_manager.buscar_contenedor('libros')
        usuarios_container = self.xml_manager.buscar_contenedor('usuarios')
        prestamos_container = self.xml_manager.buscar_contenedor('prestamos')

        if libros_container is None:
            print("Error: No se encontró el contenedor 'libros' en el XML.")
            return
        if usuarios_container is None:
            print("Error: No se encontró el contenedor 'usuarios' en el XML.")
            return
        if prestamos_container is None:
            print("Error: No se encontró el contenedor 'prestamos' en el XML.")
            return

        # Obtener todos los libros y préstamos activos
        print("\n=== LIBROS DISPONIBLES ===")
        libros = self.xml_manager.buscar_todos_hijos('libros', 'libro')
        prestamos_activos = self.xml_manager.buscar_todos_hijos('prestamos', 'prestamo')

        # Obtener IDs de libros que están prestados
        libros_prestados_ids = set()
        for prestamo in prestamos_activos:
            libro_id = self.xml_manager.obtener_atributo(prestamo, 'libro')
            libros_prestados_ids.add(libro_id)

        # Mostrar solo libros disponibles (que no están en préstamos activos)
        libros_disponibles = []
        for libro in libros:
            libro_id = self.xml_manager.obtener_atributo(libro, 'id')
            if libro_id not in libros_prestados_ids:
                nombre = self.xml_manager.obtener_texto_elemento(libro, 'nombre')
                autor = self.xml_manager.obtener_texto_elemento(libro, 'autor')
                print(f"ID: {libro_id} | Título: {nombre} | Autor: {autor}")
                libros_disponibles.append(libro)

        if not libros_disponibles:
            print("No hay libros disponibles para préstamo.")
            return

        # Solicitar ID del libro
        libro_id = input("\nIngrese el ID del libro a prestar: ")
        libro_seleccionado = self.xml_manager.buscar_elemento_por_atributo('libros', 'libro', 'id', libro_id)

        if libro_seleccionado is None:
            print("Error: Libro no encontrado.")
            return

        # Verificar que el libro esté disponible (que no esté en préstamos activos)
        if libro_id in libros_prestados_ids:
            print("Error: El libro no está disponible (ya está prestado).")
            return

        # Mostrar usuarios
        print("\n=== USUARIOS REGISTRADOS ===")
        usuarios = self.xml_manager.buscar_todos_hijos('usuarios', 'usuario')

        if not usuarios:
            print("No hay usuarios registrados.")
            return

        for usuario in usuarios:
            usuario_id = self.xml_manager.obtener_atributo(usuario, 'id')
            nombre = self.xml_manager.obtener_texto_elemento(usuario, 'nombre')
            apellidos = self.xml_manager.obtener_texto_elemento(usuario, 'apellidos')
            print(f"ID: {usuario_id} | Nombre: {nombre} {apellidos}")

        # Solicitar ID del usuario
        usuario_id = input("\nIngrese el ID del usuario: ")
        usuario_seleccionado = self.xml_manager.buscar_elemento_por_atributo('usuarios', 'usuario', 'id', usuario_id)

        if usuario_seleccionado is None:
            print("Error: Usuario no encontrado.")
            return

        # Generar ID único para el préstamo
        cantidad_prestamos = self.xml_manager.contar_elementos('prestamos', 'prestamo')
        nuevo_id = str(cantidad_prestamos + 1).zfill(3)

        # Crear el registro de préstamo
        atributos = {
            'id': nuevo_id,
            'libro': libro_id,
            'usuario': usuario_id
        }

        prestamo_creado = self.xml_manager.crear_elemento_solo_atributos('prestamos', 'prestamo', atributos)

        if prestamo_creado is not None:
            print(f"\n✓ Préstamo registrado con éxito (ID: {nuevo_id})")
            print(f"  Libro: {self.xml_manager.obtener_texto_elemento(libro_seleccionado, 'nombre')}")
            print(f"  Usuario: {self.xml_manager.obtener_texto_elemento(usuario_seleccionado, 'nombre')} "
                  f"{self.xml_manager.obtener_texto_elemento(usuario_seleccionado, 'apellidos')}")

            # Guardar cambios
            self.xml_manager.guardar_cambios()
        else:
            print("Error al crear el préstamo.")

    def devolver(self):
        """
        Elimina un registro de préstamo (devolución de libro).
        Marca el libro como disponible nuevamente.
        """
        if self.xml_manager.root is None:
            print("Error: No hay ningún fichero cargado.")
            return

        # Verificar que existe el contenedor de préstamos
        prestamos_container = self.xml_manager.buscar_contenedor('prestamos')
        if prestamos_container is None:
            print("No hay préstamos registrados.")
            return

        # Mostrar préstamos activos
        print("\n=== PRÉSTAMOS ACTIVOS ===")
        prestamos = self.xml_manager.buscar_todos_hijos('prestamos', 'prestamo')

        if not prestamos:
            print("No hay préstamos activos.")
            return

        for prestamo in prestamos:
            prestamo_id = self.xml_manager.obtener_atributo(prestamo, 'id')
            libro_id = self.xml_manager.obtener_atributo(prestamo, 'libro')
            usuario_id = self.xml_manager.obtener_atributo(prestamo, 'usuario')

            # Obtener información del libro
            libro = self.xml_manager.buscar_elemento_por_atributo('libros', 'libro', 'id', libro_id)
            nombre_libro = self.xml_manager.obtener_texto_elemento(libro, 'nombre') if libro else "N/A"

            # Obtener información del usuario
            usuario = self.xml_manager.buscar_elemento_por_atributo('usuarios', 'usuario', 'id', usuario_id)
            nombre_usuario = self.xml_manager.obtener_texto_elemento(usuario, 'nombre') if usuario else "N/A"
            apellidos_usuario = self.xml_manager.obtener_texto_elemento(usuario, 'apellidos') if usuario else ""

            print(f"ID: {prestamo_id} | Libro: {nombre_libro} | Usuario: {nombre_usuario} {apellidos_usuario}")

        # Solicitar ID del préstamo a devolver
        prestamo_id = input("\nIngrese el ID del préstamo a devolver: ")
        prestamo_seleccionado = self.xml_manager.buscar_elemento_por_atributo('prestamos', 'prestamo', 'id', prestamo_id)

        if prestamo_seleccionado is None:
            print("Error: Préstamo no encontrado.")
            return

        # Obtener el ID del libro para marcarlo como disponible
        libro_id = self.xml_manager.obtener_atributo(prestamo_seleccionado, 'libro')
        libro = self.xml_manager.buscar_elemento_por_atributo('libros', 'libro', 'id', libro_id)

        if libro is None:
            print("Error: Libro asociado al préstamo no encontrado.")
            return

        # Confirmar devolución
        nombre_libro = self.xml_manager.obtener_texto_elemento(libro, 'nombre')
        confirmacion = input(f"\n¿Confirma la devolución del libro '{nombre_libro}'? (S/N): ").upper()

        if confirmacion == 'S':
            # Eliminar el registro de préstamo
            if self.xml_manager.eliminar_hijo('prestamos', prestamo_seleccionado):
                print(f"✓ Préstamo devuelto con éxito.")
                print(f"  El libro '{nombre_libro}' está nuevamente disponible.")

                # Guardar cambios
                self.xml_manager.guardar_cambios()
            else:
                print("Error al eliminar el registro de préstamo.")
        else:
            print("Devolución cancelada.")

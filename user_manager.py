from god_xml import GodXML
from datetime import datetime

class UserManager():

    def __init__(self, xml: GodXML):
    
        self.xml = xml


    def _ask_to_continue_si_no(self, msg) -> bool: 
        ok = input(msg).upper()
        if ok in ['OK', 'SI', 'S']:
            return True
        elif ok in ['NO', 'N', 'NOP']:
            return False
        else:
            print(f'Los valores permitidos son')

    def add(self, ):
        user_id = datetime.now().strftime('%Y%m%d%H%M%S')
        self.xml.anyadir_elemento('usuarios', 'usuario', None, {'id': user_id}) 
        user_fields = [
            'nombre',
            'apellidos',
            'correo',
            'fechaNacimiento'
        ]

        for k in user_fields:
            value = input(f'Introduce tu {k}: ')
            self.xml.anyadir_elemento(f'usuarios/usuario[@id="{user_id}"]', k, value )

        self.xml.guardar_cambios()
        
    def show(self):
        usuarios = self.xml.root.find('usuarios')
        if usuarios is None or len(usuarios) == 0:
            print("No hay usuarios registrados.")
            return

        print("\n=== LISTA DE USUARIOS ===\n")
        for usuario in usuarios.findall('usuario'):
            user_id = usuario.get('id', 'Sin ID')
            print(f"ID: {user_id}")

            nombre = usuario.find('nombre')
            apellidos = usuario.find('apellidos')
            correo = usuario.find('correo')
            fechaNacimiento = usuario.find('fechaNacimiento')

            if nombre is not None:
                print(f"  Nombre: {nombre.text}")
            if apellidos is not None:
                print(f"  Apellidos: {apellidos.text}")
            if correo is not None:
                print(f"  Correo: {correo.text}")
            if fechaNacimiento is not None:
                print(f"  Fecha de Nacimiento: {fechaNacimiento.text}")
            print("-" * 40)
    
    def delete(self):
        self.show()

        user_id = input("\nIntroduce el ID del usuario a eliminar: ")

        usuario = self.xml.root.find(f'usuarios/usuario[@id="{user_id}"]')
        if usuario is None:
            print(f"No se encontró ningún usuario con ID: {user_id}")
            return

        confirmacion = self._ask_to_continue_si_no(f"¿Estás seguro de eliminar el usuario con ID {user_id}? (SI/NO): ")
        if confirmacion:
            resultado = self.xml.eliminar_elemento(f'usuarios/usuario[@id="{user_id}"]')
            if resultado:
                self.xml.guardar_cambios()
                print(f"Usuario con ID {user_id} eliminado exitosamente.")
            else:
                print("Error al eliminar el usuario.")
        else:
            print("Operación cancelada.")
    
    def search(self):
        print("\n=== BUSCAR USUARIO ===")
        print("1. Buscar por ID")
        print("2. Buscar por nombre")
        print("3. Buscar por apellidos")
        print("4. Buscar por correo")

        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == '1':
            criterio = 'id'
            valor = input("Introduce el ID del usuario: ")
        elif opcion == '2':
            criterio = 'nombre'
            valor = input("Introduce el nombre: ")
        elif opcion == '3':
            criterio = 'apellidos'
            valor = input("Introduce los apellidos: ")
        elif opcion == '4':
            criterio = 'correo'
            valor = input("Introduce el correo: ")
        else:
            print("Opción no válida.")
            return

        usuarios = self.xml.root.find('usuarios')
        if usuarios is None:
            print("No hay usuarios registrados.")
            return

        resultados = []

        for usuario in usuarios.findall('usuario'):
            if criterio == 'id':
                if usuario.get('id', '').lower() == valor.lower():
                    resultados.append(usuario)
            else:
                elemento = usuario.find(criterio)
                if elemento is not None and elemento.text and valor.lower() in elemento.text.lower():
                    resultados.append(usuario)

        if not resultados:
            print(f"\nNo se encontraron usuarios con {criterio}: {valor}")
            return

        print(f"\n=== RESULTADOS ({len(resultados)} encontrado(s)) ===\n")
        for usuario in resultados:
            user_id = usuario.get('id', 'Sin ID')
            print(f"ID: {user_id}")

            nombre = usuario.find('nombre')
            apellidos = usuario.find('apellidos')
            correo = usuario.find('correo')
            fechaNacimiento = usuario.find('fechaNacimiento')

            if nombre is not None:
                print(f"  Nombre: {nombre.text}")
            if apellidos is not None:
                print(f"  Apellidos: {apellidos.text}")
            if correo is not None:
                print(f"  Correo: {correo.text}")
            if fechaNacimiento is not None:
                print(f"  Fecha de Nacimiento: {fechaNacimiento.text}")
            print("-" * 40)
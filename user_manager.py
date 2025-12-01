from god_xml import GodXML

class UserManager():

    def __init__(self, xml):
    
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
        xml_manager =  GodXML()
        xml_manager.anyadir_elemento('usuasrios', 'usuario', None) 
        user_fields = [
            'nombre',
            'apellidos',
            'correo',
            'fechaNacimiento'
        ]

        for k in user_fields:
            value = input(f'Introduce tu {k}')
            xml_manager.anyadir_elemento('usuario', k, value ) 
        
    def show(self, ):
        return
    
    def delete(self, ):
        return
    
    def search(self, ):
        return
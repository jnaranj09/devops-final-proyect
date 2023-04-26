from variables import username
from Config_entidades import crear_entidad, eliminar_entidad, ver_entidades


def menu_inicio(username):    # Menu de inicio de sesion
    print(f"""
╔═══════════════════════════════════╗
║          Menu de Inicio           ║
╟───────────────────────────────────╢
║                                   ║
║         MENU OPTIONS:             ║
║                                   ║
║         1. Iniciar Sesion         ║
║         2. Registro               ║
║         3. Salir                  ║
║                                   ║
╚═══════════════════════════════════╝
    {username}    
    """)
    
##############################################################################################################

def main_menu(role, username, login):    # Menu principal
    if role == "admin":
        print(f"""
╔═══════════════════════════════════╗
║          Menu Principal           ║
╟───────────────────────────────────╢
║                                   ║
║            OPTIONS:               ║
║                                   ║
║         1. Inventario             ║
║         2. Configuracion          ║
║         3. Salir                  ║
║                                   ║
╚═══════════════════════════════════╝
  User: {username} 
  4. Cerrar sesion                   

""")
        opcion = input("Select an option: ")
        if opcion == "1":
            print(" Menu Inventario")
        elif opcion == "2":
            menu_configuracion()
        elif opcion == "3":
            login.logout()
        elif opcion == "4":
            login.logout()

    elif role == "user":
        print(f"""
╔═══════════════════════════════════╗
║          Menu Principal           ║
╟───────────────────────────────────╢
║                                   ║
║            OPTIONS:               ║
║                                   ║
║         1. Inventario             ║
║         2. Salir                  ║
║                                   ║
╚═══════════════════════════════════╝
  User: {username}    
  3. Cerrar sesion                   

""")
    else:
        print("Error")


##############################################################################################################

def menu_configuracion():     # Menu de configuracion
    print(f"""
╔═══════════════════════════════════╗
║          Configuracion            ║
╟───────────────────────────────────╢
║                                   ║
║            OPTIONS:               ║
║                                   ║
║         1. Inventario             ║
║         2. Sistema                ║
║         3. Salir                  ║
║                                   ║
╚═══════════════════════════════════╝
  User: {username}    
  4. Cerrar sesion                   

""")
          
##############################################################################################################
       

def config_inventario_menu():    # Menu de configuracion de inventario
    print(f"""
╔═══════════════════════════════════════╗
║      Configuracion de Inventario      ║
╟───────────────────────────────────────╢
║                                       ║
║               OPTIONS                 ║
║                                       ║
║          1. Crear Entidades           ║
║          2. Eliminar Entidades        ║
║          3. Ver Entidades existentes  ║
║          4. Que es una Entidad?       ║
║          5. Salir                     ║
║                                       ║
╚═══════════════════════════════════════╝
  User: {username}    
  6. Cerrar sesion     

""")
    opcion = input("Opcion: ")
    if opcion == "1":
        crear_entidad()
    elif opcion == "2":
        eliminar_entidad()
    elif opcion == "3":
        ver_entidades()
    elif opcion == "4":
        print("Una entidad es una columna de la tabla del inventario, se utiliza para dar atributos a los equipos.")
    else:
        print("Saliendo...")
        return False
          

##############################################################################################################


def config_administracion_menu():    # Menu de configuracion de administracion
    print(f"""
╔═══════════════════════════════════════╗
║      Administracion del Sistema       ║
╟───────────────────────────────────────╢
║                                       ║
║               OPTIONS                 ║
║                                       ║
║          1. Crear Usuarios            ║
║          2. Eliminar Usuarios         ║
║          3. Informacion de Roles      ║
║          4. Salir                     ║
║                                       ║
╚═══════════════════════════════════════╝
  User: {username}    
  5. Cerrar sesion                   

""")
    opcion = input("Opcion: ")
    if opcion == "1":
        print("Crear Usuarios")
    elif opcion == "2":
        print("Eliminar Usuarios")
    elif opcion == "3":
        print("Informacion de Roles")
    else:
        print("Saliendo...")
        return False



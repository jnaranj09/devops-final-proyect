from variables import username
from Config_entidades import crear_entidad, eliminar_entidad, ver_entidades
from Config_inventario import ver_inventario, exportar_inventario, añadir_equipo, eliminar_equipo

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
        while True:
            print(f"""
    ╔═══════════════════════════════════╗
    ║          Menu Principal           ║
    ╟───────────────────────────────────╢
    ║                                   ║
    ║            OPTIONS:               ║
    ║                                   ║
    ║         1. Inventario             ║
    ║         2. Configuracion          ║
    ║         3. Cerrar sesion          ║ 
    ║                                   ║
    ╚═══════════════════════════════════╝
      {username}                   

    """)    
            opcion = input("Select an option: ")
            if opcion == "1":
                menu_inventario()
            elif opcion == "2":
                menu_configuracion(username)
            elif opcion == "3":
                login.logout()
                break

    elif role == "user":
        while True:
            print(f"""
    ╔═══════════════════════════════════╗
    ║          Menu Principal           ║
    ╟───────────────────────────────────╢
    ║                                   ║
    ║            OPTIONS:               ║
    ║                                   ║
    ║         1. Inventario             ║
    ║         2. Cerrar Sesion          ║
    ║                                   ║
    ╚═══════════════════════════════════╝
      {username}                 

    """)
            opcion = input("Select an option: ")
            if opcion == "1":
                print(" Menu Inventario")
            elif opcion == "2":
                login.logout()
                break

##############################################################################################################

def menu_inventario():    # Menu de inventario
    while True:
            print(f"""
    ╔═══════════════════════════════════╗
    ║          Menu Inventario          ║
    ╟───────────────────────────────────╢
    ║                                   ║
    ║            OPTIONS:               ║
    ║                                   ║
    ║         1. Ver inventario         ║
    ║         2. Exportar inventario    ║
    ║         3. Añadir equipo          ║
    ║         4. Eliminar equipo        ║
    ║         5. Salir                  ║
    ║                                   ║
    ╚═══════════════════════════════════╝
      {username}                 

    """)
            opcion = input("Select an option: ")
            if opcion == "1":
                 ver_inventario()
            elif opcion == "2":
                 exportar_inventario()
            elif opcion == "3":
                 añadir_equipo()
            elif opcion == "4":
                 eliminar_equipo()
            elif opcion == "5":
                 break

##############################################################################################################

def menu_configuracion(username):     # Menu de configuracion
    while True:
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
      {username}                 

    """)
        opcion = input("Select an option: ")
        if opcion == "1":
            config_inventario_menu(username)
        elif opcion == "2":
            config_sistema_menu(username)
        elif opcion == "3":
            print("Saliendo...")
            break

          
##############################################################################################################
       
def config_inventario_menu(username):    # Menu de configuracion de inventario
    while True:
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
      {username}      

    """)
        opcion = input("Opcion: ")
        if opcion == "1":
            crear_entidad()
        elif opcion == "2":
            eliminar_entidad()
        elif opcion == "3":
            ver_entidades()
        elif opcion == "4":
            print("Una entidad es una columna de la tabla de inventario que representa un atributo de los equipos")
        elif opcion == "5":
            print("Saliendo...")
            break
          

##############################################################################################################


def config_sistema_menu(username):    # Menu de configuracion de administracion
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
  {username}         

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



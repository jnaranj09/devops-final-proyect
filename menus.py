from Config_entidades import crear_entidad, eliminar_entidad, ver_entidades
from Config_inventario import ver_inventario, exportar_inventario, añadir_equipo, eliminar_equipo
from login.login import Login
    
##############################################################################################################

def main_menu(role, username, login):    # Menu principal
    if role == "admin":
        while True:
            print(f"""
    ╔═══════════════════════════════════╗
    ║          Menu Principal           ║
    ╟───────────────────────────────────╢
    ║                                   ║
    ║            OPCIONES:              ║
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
                menu_inventario(username)
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
    ║            OPCIONES:              ║
    ║                                   ║
    ║         1. Inventario             ║
    ║         2. Cerrar Sesion          ║
    ║                                   ║
    ╚═══════════════════════════════════╝
      {username}                 

    """)
            opcion = input("Select an option: ")
            if opcion == "1":
                menu_inventario_user(username)
            elif opcion == "2":
                login.logout()
                break

##############################################################################################################

def menu_inventario(username):    # Menu de inventario para administradores
    while True:
            print(f"""
    ╔═══════════════════════════════════╗
    ║          Menu Inventario          ║
    ╟───────────────────────────────────╢
    ║                                   ║
    ║            OPCIONES:              ║
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


def menu_inventario_user(username):    # Menu de inventario para usuarios
    while True:
            print(f"""
    ╔═══════════════════════════════════╗
    ║          Menu Inventario          ║
    ╟───────────────────────────────────╢
    ║                                   ║
    ║            OPCIONES:              ║
    ║                                   ║
    ║         1. Ver inventario         ║
    ║         2. Exportar inventario    ║
    ║         3. Salir                  ║
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
                 break
   
##############################################################################################################

def menu_configuracion(username):     # Menu de configuracion
    while True:
        print(f"""
    ╔════════════════════════════════════════════╗
    ║                Configuracion               ║
    ╟────────────────────────────────────────────╢
    ║                                            ║
    ║                  OPCIONES:                 ║
    ║                                            ║
    ║         1. Configuracion de inventario     ║
    ║         2. Administracion del Sistema      ║
    ║         3. Salir                           ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
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
    ║               OPCIONES:               ║
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
            print("\nUna entidad es una columna de la tabla de inventario que representa un atributo de los equipos\n")
            input("\nPress Enter to continue...\n")
        elif opcion == "5":
            print("Saliendo...")
            break
          

##############################################################################################################


def config_sistema_menu(username):    # Menu de configuracion de administracion
    while True:
        print(f"""
    ╔═══════════════════════════════════════╗
    ║      Administracion del Sistema       ║
    ╟───────────────────────────────────────╢
    ║                                       ║
    ║               OPTIONS                 ║
    ║                                       ║
    ║          1. Crear Usuarios            ║
    ║          2. Listar Usuarios           ║ 
    ║          3. Eliminar Usuarios         ║
    ║          4. Informacion de Roles      ║
    ║          5. Salir                     ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    {username}         

    """)
        opcion = input("Opcion: ")
        if opcion == "1":
            Login.register()
        elif opcion == "2":
            Login.list_users()
        elif opcion == "3":
            Login.remove_users()
        elif opcion == "4":
            print("\n Cuando se crea un usuario, se le asigna un rol, el cual determina los permisos que tiene el usuario\n")
            print("Los roles son los siguientes: \n")
            print("admin: Tiene acceso a todas las funciones del sistema")
            print("user: Tiene acceso a ver el inventario y exportarlo en formato .xlsx \n")
            input("\nPress Enter to continue...\n")
        elif opcion == "5":
            print("Saliendo...")
            break



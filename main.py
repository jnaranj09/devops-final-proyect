from init import *
from menus import *
from login.login import *

#First check if the database exists
comprobacion_DB()

#Then check if the tables exist
comprobacion_Tablas()

#Start the app

def main():
    login = Login()

    while True:
        login.login_menu(role=login.logged_in_user.role if login.logged_in_user else None)
        option = input("Select an option: ")
        if option == "1":
            if login.login():
                username =  f"User: {login.logged_in_user.username} | Role: {login.logged_in_user.role if login.logged_in_user.role else ''}" if login.logged_in_user else ""
                main_menu(role=login.logged_in_user.role, username=username, login=login)
        elif option == "2":
            login.logout()
            quit()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
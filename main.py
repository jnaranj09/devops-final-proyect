from init import *
from menus import *
from login.login import *

#First check if the database exists
comprobacion_DB()

#Then check if the tables exist
comprobacion_Tablas()

#Start the app
def main():
    csv_file_path = '/home/jnaranjo/Documents/git/DevOps-Professional-Certification/Final Project/login/file.csv'
    login = Login(csv_file_path)

    while True:
        login.login_menu(role=login.logged_in_user.role if login.logged_in_user else None)
        option = input("Select an option: ")
        if option == "1":
            login.login()
        elif option == "2":
            login.register()
        elif option == "3":
            login.logout()
            quit()
        elif option == "4":
            login.logout()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
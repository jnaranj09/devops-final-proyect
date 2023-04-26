from init import *
from menus import *
from login.login import *

#First check if the database exists
comprobacion_DB()

#Then check if the tables exist
comprobacion_Tablas()

#Start the app
if __name__ == '__main__':
    csv_file_path = '/home/jnaranjo/Documents/git/DevOps-Professional-Certification/Final Project/login/file.csv'
    login = Login(csv_file_path)
    login.run()


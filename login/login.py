import csv
from menus import *

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class Login:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.logged_in_user = None

    def login_menu(self, role=None):
        username =  f"User: {self.logged_in_user.username} | Role: {role if role else ''}" if self.logged_in_user else ""
        menu_inicio(username)

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        with open(self.csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    self.logged_in_user = User(username, password, row[2])
                    print(f"Logged in as {username} with role {row[2]}")
                    return True

        print("Invalid username or password")
        return False

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role: ")

        with open(self.csv_file_path, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([username, password, role])

        print(f"Registered user {username} with role {role}")

    def logout(self):
        self.logged_in_user = None
        print("Logged out")



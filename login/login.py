import csv
import random

csv_file_path = '/home/jnaranjo/Documents/git/DevOps-Professional-Certification/Final Project/login/file.csv'

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class Login:
    def __init__(self):
        self.logged_in_user = None

    def login_menu(self, role=None):
        username =  f"User: {self.logged_in_user.username} | Role: {role if role else ''}" if self.logged_in_user else ""
        # Menu de inicio de sesion
        print(f"""
╔═══════════════════════════════════╗
║            BIENVENIDO             ║
╟───────────────────────────────────╢
║                                   ║
║             OPCIONES:             ║
║                                   ║
║         1. Iniciar Sesion         ║
║         2. Salir                  ║
║                                   ║
╚═══════════════════════════════════╝
    Que bendicion ve!
    {username}    
    """)

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        with open(csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[1] == username and row[2] == password:
                    self.logged_in_user = User(username, password, row[3])
                    print(f"Logged in as {username} with role {row[3]}")
                    return True

        print("Invalid username or password")
        return False

    def register():
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role: ")

        # Generate a random 4-digit number
        user_id = str(random.randint(1000, 9999))
        with open(csv_file_path, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([user_id, username, password, role])

        print(f"Registered user {username} with ID {user_id} and role {role}")

    def logout(self):
        self.logged_in_user = None
        print("Logged out")


    def list_users():
        with open(csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                 print(f"User ID: {row[0]}, User Name: {row[1]}, Role: {row[3]}")
            input("\nPress Enter to continue...\n")

    def remove_users():
        with open(csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)  # Read the contents of the file into a list
            print("\nAvailable users:\n")
            for row in rows:
                print(f"User ID: {row[0]}, User Name: {row[1]}, Role: {row[3]}")
            user_id = input("Enter user ID to delete: ")
            filtered_rows = [row for row in rows if row[0] == user_id]
            if filtered_rows:
                print(f"Found {len(filtered_rows)} matching user(s):")
                for row in filtered_rows:
                    print(f"User ID: {row[0]}, User Name: {row[1]}")
                confirm = input("Are you sure you want to delete these users? (y/n): ")
                if confirm.lower() == 'y':
                    with open(csv_file_path, "w", newline='') as csv_file:
                        writer = csv.writer(csv_file)
                        for row in rows:
                            if row not in filtered_rows:
                                writer.writerow(row)
                    print("User(s) deleted.")
            else:
                print("No users found with that ID.")


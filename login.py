import sqlite3

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "admin123":
        print("\nLogin Successful!")
    else:
        print("\nInvalid Username or Password!")

if __name__ == "__main__":
    login()

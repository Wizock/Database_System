from api import *
from session import *

def login_attemp_admin():   
    con = connect()
    while True:
        username = input("Enter username:")
        password = input("Enter password:")
        cursor = con.cursor()
        find_user_fromAdmin = cursor.execute(("SELECT * FROM admin WHERE userName = ? AND password = ?"),(username,password))
        resultsPassword = cursor.fetchall()
        if resultsPassword:
            print("Welcome :" + username)
            beginAdmin()
        else:
            print("Username or Password not found")
            print("try again")

def login_attemp_workers():   
    con = connect()
    while True:
        username = input("Enter username:")
        password = input("Enter password:")
        cursor = con.cursor()
        find_user_fromAdmin = cursor.execute(("SELECT * FROM workers WHERE userName = ? AND password = ?"), (username, password))
        firstName = cursor.execute("SELECT firstName FROM workers WHERE userName = ? ",(username,))
        resultsPassword = cursor.fetchall()
        if resultsPassword:
            print("Welcome :",list(firstName))
            break
        print("Username or Password not found")
        print("try again")

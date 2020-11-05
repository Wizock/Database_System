from api import *


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
            break
        print("Username or Password not found")
        print("try again")

def login_attemp_workers():   
    con = connect()
    while True:
        username = input("Enter username:")
        password = input("Enter password:")
        cursor = con.cursor()
        find_user_fromAdmin = cursor.execute(("SELECT * FROM workers WHERE userName = ? AND password = ?"), (username, password))
        resultsPassword = cursor.fetchall()
        if resultsPassword:
            print("Welcome :" + username)
            break
        print("Username or Password not found")
        print("try again")

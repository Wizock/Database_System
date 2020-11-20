from api import *
from login import *
from session import * 
import sqlite3

def login_attemp_admin():
    global username, password   
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


def main():
    
    permission = checkIfEmpty()

    if permission == True:
        con = connect()
        createTableFormat()
        admin_register()

    if permission == False:
        con = sqlite3.connect('main_Database.db')
        createTableFormat()
        admin_register()
        
    adminOrNot = input("are you a worker or a admin?| type 'admin' or 'worker': ")

    if adminOrNot == "admin":
        
        print("please Login:\n")
        login_attemp_admin()
    if adminOrNot == 'worker':
        print("please Login:\n")
        login_attemp_workers()  
if __name__=="__main__":
    main()


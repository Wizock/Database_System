from api import *
from login import *
from session import * 
import sqlite3

def main():
    
    permission = checkIfEmpty()

    if permission == True:
        con = connect()
        createTableFormat()

    if permission == False:
        con = sqlite3.connect('main_Database.db')
        createTableFormat()
        
    adminOrNot = input("are you a worker or a admin?| type 'admin' or 'worker': ")

    if adminOrNot == "admin":
        
        print("please Login:\n")
        login_attemp_admin()


    if adminOrNot == 'worker':
        print("please Login:\n")
        login_attemp_workers()    
if __name__=="__main__":
    main()

admin

WizockAdmin
Admin123

Rohaan

Ahmed

rahm0@eq.edu.au

17

grills


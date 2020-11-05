from api import *
from login import *
import sqlite3

def main():
    
    permission = checkIfEmpty()
    status = status

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
        status = adminOrNot

    if adminOrNot == 'worker':
        print("please Login:\n")
        login_attemp_workers()
        status = adminOrNot
    if status == 'admin':

    
if __name__=="__main__":
    main()
k

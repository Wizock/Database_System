import sqlite3
from sqlite3 import Error
import os

def admin_register():
    con = connect()
    try:
        con.execute('''
            INSERT INTO Admin (email,userName,password) VALUES (?,?,?)
        ''',("Wizock.Admin@mail.com","admin","admin"))
        con.commit()
        con.close()
        print("your Admin account has been created :)")
    except Error as e:
        print(e)

def createTableFormat():
    conn1 = connect()
    try:
        conn1.execute('''        
            CREATE TABLE workers (
                firstName varchar(255),
                lastName varchar(255),
                email varchar(255),
                userName varchar(255),
                password varchar(255),
                Age int,
                Wage int,
                position varchar(255),
                UserId int,
                FOREIGN KEY (UserId) REFERENCES Admin(UserId)
                )
            ''')

        conn1.execute('''
            CREATE TABLE Admin (
                UserId INTEGER PRIMARY KEY,
                email varchar(255),
                userName varchar(255),
                password varchar(255)
                )
                ''')
        # this is a query which creates a table, this specific query sets up the table's format
        check_Admin = conn1.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Admin'")
        check_Workers = conn1.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='workers'")
        
        if check_Admin != None:
            conn1.execute("DROP TABLE Admin")
        if check_Workers != None:
            conn1.execute("DROP TABLE workers")
    except Error as e:
        print(e)

        
def connect():
    Path = os.getcwd()+"\main_DataBase.db"
    if Path != os.path.islink(Path):
        con = sqlite3.connect(Path)
        
    return con

def checkIfEmpty():
    Path = os.getcwd()+"\main_DataBase.db"
    if os.path.exists(Path) == True:
        return False
    else:
        return True
        
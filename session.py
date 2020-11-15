import random
import string
from api import *
from main import main

positions = ["grills","front","assembly","drive_through","cleaning"]
connection = connect()

def beginAdmin():
    regOrDel = input("would you like to edit or delete a employee:")
    if regOrDel == "edit":
        edit()
    if regOrDel == "delete":
        delete()

def userName():
    for i in range(0,3):
        userName = str(register_firstName[i]+str(random.randint(0,999))+str(random.randint(0,999))+str(random.randint(0,999)))
    return userName

def password():
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(3))+str(random.randint(0,3))+str(random.randint(0,999))+str(random.randint(0,999))
    return result_str

def calculateWage():
    payingFactor = 20
    workingTime = 9
    age = register_age
    positionValue = 10
    position = list(register_position)
    for Positions in positions:
        for i in range(0,len(Positions)):
            if register_position == positions[0]:
                positionValue += 25
            elif register_position == positions[1]:
                positionValue += 29
            elif register_position == positions[2]:
                positionValue += 18
            elif register_position == positions[3]:
                positionValue += 15
            elif register_position == positions[4]:
                positionValue += 26

    wage = int(age*payingFactor/workingTime+positionValue)

    return wage

def delete():
    employees = list(connection.execute("SELECT firstName FROM workers"))
    position = list(connection.execute("SELECT position FROM workers"))
    wage = list(connection.execute("SELECT wage FROM workers"))
    employeeID = list(connection.execute("SELECT employeeID FROM workers"))
    for i in range(0,len(employees)):
        print(employeeID[i]+":"+employees[i]+":"+position[i]+":"+wage[i])
    employeeToDel = int(input("Which employee would you like to delete? :"))
    connection.execute("DELETE ? FROM workers"),(employees[employeeToDel])



def edit():
    global register_firstName, register_lastName, register_position,register_age,register_position

    register_firstName = input("enter Employee's First Name:")
    register_lastName = input("enter Employee's Last Name:")
    register_email = input("Enter Employee's email:")
    # make User name primary on both tables
    register_userName  = userName()
    register_password = password()
    register_age = int(input("Enter Employee's age:"))
    register_position = input("Enter the assigned Employee's position:")
    if register_position not in positions:
        print("this position is not valid")
        register_position = input("Enter the assigned Employee's position:")
    register_Wage = calculateWage()

    registerNother = input("would you like to register another worker? | type: 'yes' or 'no' :")
    if registerNother == "yes":
        connection.execute('''
        INSERT INTO employee_personal (firstName,lastName,email,userName,password,Age,Wage,position)
        VALUES (?,?,?,?,?,?,?,?)
        ''',
        (register_firstName,register_lastName,register_email,register_userName,register_password,register_age,register_Wage,register_position))
        connection.commit()
        edit()
    if registerNother == 'no':
        connection.execute('''
        INSERT INTO employee_personal (firstName,lastName,email,userName,password,Age,Wage,position)
        VALUES (?,?,?,?,?,?,?,?)
        ''',
        (register_firstName,register_lastName,register_email,register_userName,register_password,register_age,register_Wage,register_position))
        connection.commit()
        connection.close()
    again = input("would you like to logout? :")
    if again == "yes":
        main()
    elif again == 'no':
        beginAdmin()


class Manager_session:
    def __init__(self):
        self.connection = connect()
        self.SessionTime = clock()
    def begin(self):
        while self.SessionTime < 25:
            pass
    def render_session(self):
        pass

class Worker_session:
    def __init__(self):
        self.connection = connect()
        self.SessionTime = clock()
    def begin(self):
        while self.SessionTime < 25:
            pass
    def render_session(self):
        pass
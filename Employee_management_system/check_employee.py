import employee_details
import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

def list_employees():
    # rows = cursor.execute("SELECT id, name, salary, designation, workinghours FROM employee ").fetchall()
    # print(rows)
    
    print('\nColumns in EMPLOYEE table:')
    data=cursor.execute('''SELECT * FROM EMPLOYEE''')
    for column in data.description:
        print(column[0])

    print("Data in the table : \n")
    rows = cursor.execute("SELECT * FROM employee").fetchall()
    print(rows)
    
        
    
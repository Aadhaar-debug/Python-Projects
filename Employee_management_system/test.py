import sqlite3
from contextlib import closing

connection = sqlite3.connect("employee.db")

print(connection.total_changes)

cursor = connection.cursor()
cursor.execute("CREATE TABLE employee (id INTEGER, name TEXT, salary INTEGER , designation TEXT , workinghours INTEGER)")

cursor.execute("INSERT INTO employee VALUES ('1', 'Elon', '130000000' , 'RocketScientist' , '80')")
cursor.execute("INSERT INTO employee VALUES ('2', 'Jeff', '100000000', 'Businessman', '50')")
cursor.execute("INSERT INTO employee VALUES ('3', 'Mukesh', '110000000', 'Businessman', '60')")
cursor.execute("INSERT INTO employee VALUES ('4', 'Bill', '11000000', 'Technician', '30')")

rows = cursor.execute("SELECT id , name , salary , designation , workinghours FROM employee").fetchall()
print(rows)

employee_name = "jeff"
rows = cursor.execute(
    "SELECT id , name , salary , designation , workinghours FROM employee WHERE name = ?",
    (employee_name,),
).fetchall()
print(rows)

new_designation = 'Businessman'
employee_name = "jeff"
cursor.execute(
    "UPDATE employee SET designation = ? WHERE name = ?",
    (new_designation, employee_name)
)

rows = cursor.execute("SELECT id , name , salary , designation , workinghours FROM employee").fetchall()
print(rows)

employee_name = "Bill"
cursor.execute(
    "DELETE FROM employee WHERE name = ?",
    (employee_name,)
)

rows = cursor.execute("SELECT id , name , salary , designation , workinghours FROM employee").fetchall()
print(rows)


with closing(sqlite3.connect("employee.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)
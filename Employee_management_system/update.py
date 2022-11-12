import sqlite3
import greeting
connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

def update_employee_info():
    greeting.Update_greet()
    print("Changing the employee informaton - Designation from Rocketseientist to businessman ")
    new_designation = 'Businessman'
    employee_name = "Elon"
    cursor.execute(
        "UPDATE employee SET designation = ? WHERE name = ?",
        (new_designation, employee_name)
    )
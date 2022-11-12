import choice
import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

class employee:
    def employee_info():
        print("Entering the values for : Elon , Jeff , Mukesh and Bill")
        print("Values for ELon : '1', 'Elon', '130000000' , 'RocketScientist' , '80'")
        print("Values for Jeff : '2', 'Jeff', '100000000', 'Businessman', '50')")
        print("Values for Mukesh : '3', 'Mukesh', '110000000', 'Businessman', '60')")
        print("Values for Bill : '4', 'Bill', '11000000', 'Technician', '30')")
        cursor.execute("INSERT INTO employee VALUES ('1', 'Elon', '130000000' , 'RocketScientist' , '80')")
        cursor.execute("INSERT INTO employee VALUES ('2', 'Jeff', '100000000', 'Businessman', '50')")
        cursor.execute("INSERT INTO employee VALUES ('3', 'Mukesh', '110000000', 'Businessman', '60')")
        cursor.execute("INSERT INTO employee VALUES ('4', 'Bill', '11000000', 'Technician', '30')")
        # cursor.execute("INSERT INTO employee VALUES ('Sammy', 'shark', 1)")
        # cursor.execute("insert into employee (id , name , salary , designation , workinghours ) values (?, ?, ?, ?, ?)",(employee_id , employee_name , employee_salary , employee_designation , employee_working_hours))
        # cursor.commit()

        print("\n----------------------------------------------------------------------")
        print("------------EMPLOYEE INFORMATION SAVED SUCCESSFULLY !!!---------------- ")
        print("----------------------------------------------------------------------\n")


        choice.choose()
        

# class remove_employee(employee):
#     def remove_employee():
#         id = int(input("Enter the employee id that you want to remove out : "))
#         employee[id].delete()
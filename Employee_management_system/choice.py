import employee_details
import greeting
# import sql_connector
from time import sleep
import check_employee
import update


def choose():
    sleep(1)
    option = int(input("Choose what operation do you want to perform ? \n1.Enter Employee \n2.Update employees \n3.List employees\n4.Delete employee\n5.Exit\n"))
    
    if(option == 1):
        employee_details.employee.employee_info()
        return 0

    if(option == 2):
        
        update.update_employee_info()

        return 0

    if(option == 3):
        sleep(2)
        check_employee.list_employees()
        print("----------------------Listing the Employees...-------------------")
        
        return 0

    if(option == 4):
        sleep(2)

        print("----------------------Deleting the Employees...-------------------")
        return 0

    if(option == 5):
        sleep(2)

        print("----------------------Listing the Employees...-------------------")
        return 0
    
    else:
        sleep(2)

        print("\n----------------------------------------------------------------------")
        print("THERE IS NO OPTION FOR THE SPECIFIED INPUT PLEASE TRY AGAIN WITH A VALID INPUT ")
        print("----------------------------------------------------------------------\n")

        choose()
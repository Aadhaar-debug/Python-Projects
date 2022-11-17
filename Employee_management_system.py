# employee management system using the concept of classes and objects 
# Made by aadhaar koul 5th semester cse dept.

# creating the parent employee class 
class employee:
    def input_information(self):

        number_of_employees = int(input("Enter the number of employees whose information you wan to enter ! \n"))

        employee[number_of_employees]

        print("\n------------------Start entering the information of the employees : ------------------------\n")
        for i in range(number_of_employees):
            self.employee[i].id = int(input("Enter the id of the employee : \n"))
            self.employee[i].name = int(input("Enter the name of the employee : \n"))
            self.employee[i].designation = int(input("Enter the designation of the employee : \n"))
            self.employee[i].working_Hours = int(input("Enter the working_Hours of the employee : \n"))
        print("\n-----------------------Employees information saved successfully !!!-------------------------\n")

# creating the remove class to remove employees from the parent class 
class remove_employee(employee) : 
    def remove(self):
        remove_id = int(input("Enter the id of the employee whose information you want to remove !!!-------\n"))
        employee[remove_id].id = "NA"
        employee[remove_id].name = "NA"
        employee[remove_id].designation = "NA"
        employee[remove_id].working_Hours = "NA"


# Creating the promote class to promote employees from the current designation 
class promote_employees(employee):
    def promote(self):
        promote_id = input("Enter the employee id that you want to promote")
        promotion_designation = "Software Developer"
        employee[promote_id].designation = promotion_designation

class software_developer(employee):
    def store_software_engineers(self):
        software_developer = []
        for i in range(employee):
            if(employee[i].designation == "Software Engineer"):
                software_developer += employee[i].id

        def list_software_developers():
            for i in range(employee):

                print("\nEmployee " + employee[i].id + "\n")

                list_software_developers()


class Front_end_engineer(employee) :
    def store_Front_end_engineers(self):
        Front_end__developer = []
        for i in range(employee):
            if(employee[i].designation == "Front end engineer"):
                software_developer += employee[i].id

        def list_Front_end_engineer(self):
            for i in range(employee):

                print("\nEmployee " + employee[i].id + "\n")

                list_Front_end_engineer()

class Backend_engineer(employee) :
    def store_Backend_engineer(self):
        Backend_engineer = []
        for i in range(employee):
            if(employee[i].designation == "Backend engineer"):
                software_developer += employee[i].id

        def list_Backend_engineer(self):
            for i in range(employee):

                print("\nEmployee " + employee[i].id + "\n")

                list_Backend_engineer()

# Main execution class 
class start(employee):
    
    def main() : 
        choice = input("\nChoose from te following list \n1 to Add Employeess \n2 to Remove the employees \n3 to Promote employees \n4 to Display Employees\n")
        if(choice == 1):
            employee.input_information()
        if(choice == 2):
            remove_employee.remove()
        if(choice == 3):
            promote_employees.promote()
        if(choice == 4):
            print("\nListing all employees !!!\n")
            # for i in range(employee[number_of_employees]):
            #     print("new ")

# Programme begins 
start.main()




# Employee management system using classes and objects 
# Made by Aadhaar Koul 
# 3rd year student in MIET Jammu
#
#
#
#

class Employee:
    def __init__(self):
        self.name = "Elon"
        self.id = "1"
        self.designation = "Web Developer"
        self.Working_hours = "35"

    def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)

    def Remove_Employee(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"

    def Promote_Employee(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"


class FrontEnd_Engineer(Employee):
  def __init__(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"
  def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)

class Software_Engineer(Employee):
  def __init__(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"
  def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)

class Backend_Engineer(Employee):
  def __init__(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"
  def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)



emp = Employee()
SDE = Software_Engineer()
FEE = FrontEnd_Engineer()
BEE = Backend_Engineer()


def main():
  choice = int(input("\nEnter the coresponding number to select the desired option\n1. To display Employee \n2. To promote Employee\n3. To remove Employees\n4. To add EMployees\n5. To Exit the program\n\n"))
  if(choice == 1):
    emp.Display_Employee()

  if(choice == 2):
    emp.id == SDE.id
    emp.name == SDE.name
    emp.designation == SDE.designation
    emp.Working_hours == SDE.Working_hours
    print("Identity number of the employee = " + SDE.id)
    print("Name of the employee = " + SDE.name)
    print("Position of the employee of the employee = " + SDE.designation)
    print("Woking hours of the employee = " + SDE.Working_hours)
    print("\nEmploye Promoted successfully\n")

  if(choice == 3):
    emp.Remove_Employee()
    emp.name = "_"
    emp.id = "_"
    emp.designation = "_"
    emp.Working_hours = "_"

    print("Employee Removed successfully !!!")

  if(choice == 4):
    print("Employee details initialized successfuly !!!\n")
    emp.Display_Employee()
    print("\nEmployee Identity added successfully !!!")

  if(choice == 5):
    print("See ya !!!")
    return 0

  else:
    print(".")

  main()

main()

# simple calculator using the cocept of function and swwith cases 
# made by aadhaar koul , 5th semester , cse dept.


# function to add two numbers
def addition():
  # taking the inputs first  
  a = int(input("Enter the first number "))
  b = int(input("Enter the second number "))
  print("\nThe sum of the two number s is equal to = " , int(a+b))
  print("\n")



# function to subtract two numbers 
def subtraction():

  # taking the inputs first  
  a = int(input("Enter the first number "))
  b = int(input("Enter the second number "))
  print("\nThe delifference of the two number s is equal to = " , int(a-b))
  print("\n")



# function to multiply two numbers
def multiplication():

  # taking the inputs first  
  a = int(input("Enter the first number "))
  b = int(input("Enter the second number "))
  print("\nThe product of the two number s is equal to = " , int(a*b))
  print("\n")


# functiont o divide two numbers 
def division():

  # taking the inputs first  
  a = int(input("Enter the first number "))
  b = int(input("Enter the second number "))
  print("\nThe remainder of the two number s is equal to = " , float(a/b))
  print("\n")


# main function from where the main program will execute
def main():
  choice = int(input("\n Choose from the following options \n1 for addition \n2 for subtraction \n3 for multiplication \n4 for division \n5 to quit the programme \n"))
  
  # switch cases for execution of different methods 
  match choice:

    case 1:
      # this case will execute the addition function
        addition()

    case 2:
      # this case will execute the subtraction function

        subtraction()

    case 3:
      # this case will execute the multiplication function

        multiplication()
    
    case 4:
      # this case will execute the division function

        division()
    
    case 5:
      # this case will end the programme execution

        return 0

    case _:
      # in case the input is not included in the response case 
        print("\nINVALID Input try again !!!\n")
        main()
   
# executio of the main function at the beginning of the programme 
main()

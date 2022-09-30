# importing the numbers library to perform the string like operations on the integers
import numbers

# used to make the code more attractive
print(" ")


# taking the input
A = int(input("Enter a number : "))


# a complete function / process through which the non palindrome number will 
# be processed again and again until it becomes a palindrome number
def process(a):
    num = a
    number = a
    reversed_num = 0

#  reversing the number   
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
        
        
# adding the reversed number to the original number 
    print("Reversed Number: " , reversed_num)
    added_number = reversed_num + number
    print("Added number = ", added_number)

    
#   Checking if the added number is a palindrome or not ?
    checking_number = str(added_number)
    if checking_number == checking_number[::-1]:  
            print('The given number is PALINDROME')  
            print(" ")

    else:  
        print('The added number is NOT a palindrome')
        print(" ")
        print('Repeating the process')
        
        
#   processing the added number through the function again until the number becomes a palindrome
        temp = added_number
        process(temp)


process(A)
        

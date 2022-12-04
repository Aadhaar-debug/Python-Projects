a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
c = int(input("Enter the third number\n"))

def max_of_three_numbers(a,b,c):

    if (a >= b) and (a >= b):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
     largest = c
    print("The largest number is", largest)
    print("\n")


def armstrong_or_not(num):
    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
    if num == sum:
     print(num,"is an Armstrong number\n")
    else:
     print(num,"is not an Armstrong number\n")

# calling the functions for the execution
max_of_three_numbers(a,b,c)

# checking armstrong or not for the first number 
armstrong_or_not(a)
# checking armstrong or not for the second number 
armstrong_or_not(b)
# checking armstrong or not for the third number 
armstrong_or_not(c)

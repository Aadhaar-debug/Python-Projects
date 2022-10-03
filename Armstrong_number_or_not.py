# Python program to check if the number is and armstrng number or not
num = int(input("Enter the number that you wna to find the amstrong number : "))

# Changed num variable to string, 
# and calculated the length (number of digits)
string = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** string
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

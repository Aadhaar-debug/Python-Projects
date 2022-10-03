#  Reversing a number using while loop
num = int(input("Enter a number : "))
reversed_num = 0

while num != 0 :
    reversed_num = reversed_num * 10 + digit
    digit = num % 10
    num //= 10

print("Reversed Number = " + str(reversed_num))

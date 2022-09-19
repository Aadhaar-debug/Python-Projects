# This program add the digits of a specified number and then prints the sum of the digits as the output

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)
